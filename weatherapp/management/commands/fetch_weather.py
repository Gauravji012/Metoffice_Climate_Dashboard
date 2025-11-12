import requests
from django.core.management.base import BaseCommand
from weatherapp.models import WeatherData
from datetime import datetime

class Command(BaseCommand):
    help = "Fetch and parse UK MetOffice weather data and store in database"

    # URL for UK Tmax data
    DATA_URL = "https://www.metoffice.gov.uk/pub/data/weather/uk/climate/datasets/Tmax/date/UK.txt"

    def handle(self, *args, **kwargs):
        self.stdout.write("Fetching weather data from UK MetOffice...")
        
        try:
            # Download the data
            response = requests.get(self.DATA_URL, timeout=10)
            response.raise_for_status()
            lines = response.text.splitlines()
            
            self.stdout.write(f"Downloaded {len(lines)} lines of data")
            
            # Clear existing data for UK Tmax to avoid duplicates
            WeatherData.objects.filter(region='UK', parameter='Tmax').delete()
            
            # Parse and store data
            count = 0
            for line in lines[7:]:  # Skip first 7 header lines
                line = line.strip()
                if not line or line.startswith('---'):
                    continue
                
                parts = line.split()
                if len(parts) < 13:  # Need at least year + 12 months
                    continue
                
                try:
                    year = int(parts[0])
                    
                    # Parse monthly values (columns 1-12 are Jan-Dec)
                    for month_index in range(1, 13):
                        value_raw = parts[month_index].strip()
                        
                        # Skip empty or invalid values
                        if value_raw == '' or value_raw == '---':
                            continue
                        
                        value = float(value_raw)
                        
                        # Create date object (first day of each month)
                        date = datetime(year, month_index, 1).date()
                        
                        # Save to database
                        WeatherData.objects.create(
                            date=date,
                            region='UK',
                            parameter='Tmax',
                            value=value
                        )
                        count += 1
                        
                except (ValueError, IndexError) as e:
                    self.stdout.write(f"Skipping invalid line: {line[:50]}... Error: {e}")
                    continue
            
            self.stdout.write(self.style.SUCCESS(f"Successfully stored {count} weather records in database!"))
            
        except Exception as e:
            self.stdout.write(self.style.ERROR(f"Error fetching data: {e}"))

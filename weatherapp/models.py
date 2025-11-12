from django.db import models

class WeatherData(models.Model):
    date = models.DateField()  # The date (year-month-day)
    region = models.CharField(max_length=100)  # e.g., "UK", "England", "Scotland"
    parameter = models.CharField(max_length=50)  # e.g., "Tmax", "Tmin", "Rainfall"
    value = models.FloatField()  # The weather value (temperature, rainfall, etc.)

    class Meta:
        ordering = ['date']
        unique_together = ['date', 'region', 'parameter']  # Prevent duplicate entries

    def __str__(self):
        return f"{self.date} | {self.region} | {self.parameter}: {self.value}"

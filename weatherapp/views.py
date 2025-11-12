from rest_framework import viewsets, filters, status
from rest_framework.decorators import action
from rest_framework.response import Response
from weatherapp.models import WeatherData
from weatherapp.serializers import WeatherDataSerializer
from django.shortcuts import render

class WeatherDataViewSet(viewsets.ModelViewSet):
    """
    API endpoint for weather data.
    Allows filtering by region, parameter, and date range.
    """
    queryset = WeatherData.objects.all()
    serializer_class = WeatherDataSerializer
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['region', 'parameter']
    ordering_fields = ['date', 'region']
    ordering = ['-date']

    def get_queryset(self):
        """
        This method allows filtering the queryset based on query parameters.
        """
        queryset = WeatherData.objects.all()
        
        # Filter by region (e.g., ?region=UK)
        region = self.request.query_params.get('region', None)
        if region:
            queryset = queryset.filter(region=region)
        
        # Filter by parameter (e.g., ?parameter=Tmax)
        parameter = self.request.query_params.get('parameter', None)
        if parameter:
            queryset = queryset.filter(parameter=parameter)
        
        # Filter by date range (e.g., ?start_date=2020-01-01&end_date=2024-12-31)
        start_date = self.request.query_params.get('start_date', None)
        end_date = self.request.query_params.get('end_date', None)
        
        if start_date:
            queryset = queryset.filter(date__gte=start_date)
        if end_date:
            queryset = queryset.filter(date__lte=end_date)
        
        return queryset

    @action(detail=False, methods=['get'])
    def regions(self, request):
        """
        Custom endpoint to get all available regions.
        Usage: /api/weather/regions/
        """
        regions = WeatherData.objects.values_list('region', flat=True).distinct()
        return Response({'regions': list(regions)})

    @action(detail=False, methods=['get'])
    def parameters(self, request):
        """
        Custom endpoint to get all available parameters (Tmax, Tmin, etc.).
        Usage: /api/weather/parameters/
        """
        parameters = WeatherData.objects.values_list('parameter', flat=True).distinct()
        return Response({'parameters': list(parameters)})

    @action(detail=False, methods=['get'])
    def latest(self, request):
        """
        Get the latest weather data.
        Usage: /api/weather/latest/
        """
        latest_data = WeatherData.objects.order_by('-date').first()
        serializer = self.get_serializer(latest_data)
        return Response(serializer.data)

def dashboard(request):
    """
    Render the weather dashboard page.
    """
    return render(request, 'weatherapp/dashboard.html')    
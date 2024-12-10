from django.shortcuts import render
from .models import Data
from django.http import HttpResponse
from django.db.models import Count
from django.db.models import Avg

# Create your views here.
def chart_view(request):
    
    # Aggregate count of occurrences of each country
    country_counts = (
        Data.objects.values('country')  # Group by 'country'
        .annotate(count=Count('country'))    # Count occurrences
        .order_by('-count')[:10]            # Sort by count and limit to top 10
    )

    # Prepare data for the chart1
    labels1 = [item['country'] for item in country_counts]
    values1 = [item['count'] for item in country_counts]
    #Prepare data for the chart2
    top_sectors = (Data.objects.values('sector')
                    .annotate(avg_intensity=Avg('intensity'))  # Assuming intensity is a field in the model
                    .order_by('-avg_intensity')[:10])
    labels2=[item['sector'] for item in top_sectors]
    for k in range(len(labels2)):
        if labels2[k]==None:
            labels2[k]="Unknown" 
    
    values2=[item['avg_intensity'] for item in top_sectors]
    #Prepare data for chart3
    region_counts=(Data.objects.values('region')
                        .annotate(count=Count('country'))    # Count occurrences
                        .order_by('-count')[:6]   )  
    labels3 = [item['region'] for item in region_counts]
    values3 = [item['count'] for item in region_counts]
    #Prepare data for chart4
    top_start_years = (Data.objects.values('start_year')
                    .annotate(avg_intensity=Avg('intensity'))  # Assuming intensity is a field in the model
                    .order_by('-avg_intensity')[:10])
    labels4=[item['start_year'] for item in top_start_years]
    values4=[item['avg_intensity'] for item in top_start_years]

    #Prepare data for chart5
    top_end_years = (Data.objects.values('end_year')
                    .annotate(avg_intensity=Avg('intensity'))  # Assuming intensity is a field in the model
                    .order_by('-avg_intensity')[:10])
    labels5=[item['end_year'] for item in top_end_years]
    values5=[item['avg_intensity'] for item in top_end_years]
    #Prepare data for chart6
    # Aggregate average impact for each pestle category
    pestle_impact_data = (
         Data.objects
        .values('pestle')  # Group by pestle
        .annotate(avg_impact=Avg('impact'))  # Calculate average impact
        .order_by('-avg_impact') [:6] # Sort by impact
    )

    # Prepare data for the chart
    labels6 = [item['pestle'] for item in pestle_impact_data]  # X-axis: Pestle categories
    values6 = [item['avg_impact'] for item in pestle_impact_data]  # Y-axis: Avg impacts



    return render(request, 'myapp/index.html', {'labels1': labels1, 'values1': values1,
                                                'labels2':labels2,'values2':values2,'labels3':labels3,'values3':values3,
                                                'labels4':labels4,'values4':values4,
                                                'labels5':labels5,'values5':values5,
                                                'labels6':labels6,'values6':values6})


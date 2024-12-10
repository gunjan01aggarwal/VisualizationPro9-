from django.urls import path
from MyApp import views

urlpatterns = [
    path("charts/",views.chart_view,name="chart_view")
]
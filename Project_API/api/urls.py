from django.urls import path
from .views import CompanyViews

app_name= 'api'
urlpatterns = [
    path('companies/', CompanyViews.as_view(), name='companiesList'),
    path('companies/<int:id>', CompanyViews.as_view(), name='companiesProcess')
]


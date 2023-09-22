from django.urls import path
from . import views



urlpatterns = [
    path('productslist', views.ProductListView.as_view()),
    path('search', views.SearchProductView.as_view()),

]
from django.urls import path
from . import views

urlpatterns = [
    path('', views.NewsListView.as_view(), name='news_list'),
    path('<int:news_id>/', views.NewsDetailsView.as_view(), name='news_detail'),
]

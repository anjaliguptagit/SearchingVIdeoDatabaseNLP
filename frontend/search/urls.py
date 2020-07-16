from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
	path('', views.home, name='search_home'),
	path('results.html', views.results, name='search_results'),
]

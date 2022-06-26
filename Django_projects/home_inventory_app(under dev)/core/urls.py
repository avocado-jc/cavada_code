from django.urls import path
from . import views

app_name = 'core' # for namespacing
urlpatterns = [
    path('', views.index, name='index'),
    # path('', views.details, name='details'),
    # path('', views.results, name='results'),
    # path('', views.voting, name='voting'),
]
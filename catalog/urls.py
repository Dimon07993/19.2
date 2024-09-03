#from django.urls import path


#from catalog.views import index

#urlpatterns = [
#    path('', index, name='index'),
#]

from django.urls import path
from catalog.views import home_view, contact_view

urlpatterns = [
    path('', home_view),
    path('', contact_view),
]
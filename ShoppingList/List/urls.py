from django.urls import path
from . import views 

#The appenders to the URLs in (the other) urls.py

urlpatterns = [                           #Essentially this is where we create the extensions for the URLs THAT were defined in urls.py (the other one).
    path('', views.index, name='index'),  #This means that 127.0.0.1:800/ or 127.0.0.1:800/index (depending on what is defined in urlspatterns in the other urls.py) will display the index.html code
    path('add/', views.add, name='add_the_product'),
    path('edit/<int:product_id>', views.edit, name="edit"),
    path('delete/<int:product_id>', views.delete, name='delete'),  #Need a URL because I am going to use this to call from index.html in order to get to the views.py functions
    path('sorting/<str:sort_value>', views.sorting, name="sort"),  #Unlike py4web we literally need a URL for every view that is called from index.html
    
]
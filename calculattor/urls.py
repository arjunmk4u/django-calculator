from django.urls import path, include

from . import views
urlpatterns = [
    path('calc/', views.calc),
    # path('',views.calc, name='add')
    
]
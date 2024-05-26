from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about', views.about, name='about'),
    path('api/v1/whells/cars/', include([
        path('<int:car_id>/blur-image', views.blur_image, name='blur_image'),
        path('<int:car_id>', views.show_car, name='show_car'),
        path('create', views.create_car, name='create_car'),
    ])),
]

from django.shortcuts import render
from django.http import JsonResponse
from django.core.exceptions import ObjectDoesNotExist
import numpy as np
import cv2
from django.views.decorators.csrf import csrf_exempt
from .models import Car
from .serializers import CarSerializer
import base64


@csrf_exempt
def blur_image(request, car_id):
    return JsonResponse({"error": "Invalid request"}, status=400)


def home(request):
    return render(request, "home.html")


def show_car(request, car_id):
    try:
        car = Car.objects.get(id=car_id)
    except ObjectDoesNotExist:
        return JsonResponse({"error": "Sorry, the car not found."}, status=404)

    serializer = CarSerializer(car)
    return JsonResponse({"car": serializer.data}, status=200)

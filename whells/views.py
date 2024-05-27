import json
from django.shortcuts import render
from django.http import JsonResponse
from django.core.exceptions import ObjectDoesNotExist
from rest_framework.decorators import api_view
from django.views.decorators.csrf import csrf_exempt
from .models import Car
from .serializers import CarSerializer
from .constants import ABOUT_DATA
from .services import ImageBlurService


def home(request):
    return render(request, "home.html")


def about(request):
    context = {"about_data": ABOUT_DATA}
    return render(request, "about.html", context)


def show_car(request, car_id):
    try:
        car = Car.objects.get(id=car_id)
    except ObjectDoesNotExist:
        return JsonResponse({"error": "Sorry, the car not found."}, status=404)

    serializer = CarSerializer(car)
    return JsonResponse({"car": serializer.data}, status=200)


@csrf_exempt
@api_view(["POST"])
def create_car(request):
    if request.method == "POST":
        try:
            request_data = json.loads(request.body)
            serializer = CarSerializer(data=request_data)
            if serializer.is_valid():
                serializer.save()
                return JsonResponse(serializer.data, status=201)
            return JsonResponse(serializer.errors, status=400)
        except json.JSONDecodeError:
            return JsonResponse(
                {"error": "Invalid JSON format in request body"}, status=400
            )
    else:
        return JsonResponse({"error": "Method not allowed"}, status=405)


@csrf_exempt
@api_view(["POST"])
def blur_image(request, car_id):
    if request.method == "POST":
        try:
            request_data = json.loads(request.body)
            image_path = request_data.get("image_path")
            obj = ImageBlurService(car_id, image_path)
            result = obj.apply_blur_effect()

            return JsonResponse(result, status=200 if result["success"] else 400)
        except Exception as e:
            print(f"Exception: {e}")
            return JsonResponse({"error": f"Error: {e}"}, status=400)
    else:
        return JsonResponse({"error": "Only post method is allowed."}, status=405)

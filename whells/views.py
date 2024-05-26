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
    # if request.method == 'POST':
    #     # Assuming image data is sent in base64 format from Laravel
    #     image_data = request.POST.get('image_data')
    #     if image_data:
    #         image_bytes = base64.b64decode(image_data)
    #         image_np = np.frombuffer(image_bytes, dtype=np.uint8)
    #         image = cv2.imdecode(image_np, flags=cv2.IMREAD_COLOR)

    #         # Process the image
    #         plate_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_russian_plate_number.xml')
    #         gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    #         plates = plate_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))
    #         for (x, y, w, h) in plates:
    #             roi = image[y:y+h, x:x+w]
    #             blurred_roi = cv2.GaussianBlur(roi, (25, 25), 0)
    #             image[y:y+h, x:x+w] = blurred_roi

    #         # Convert processed image back to base64 for response
    #         _, img_encoded = cv2.imencode('.jpg', image)
    #         img_base64 = base64.b64encode(img_encoded).decode('utf-8')

    #         return JsonResponse({'processed_image': img_base64})

    # return JsonResponse({'error': 'Invalid request'}, status=400)


def home(request):
    return render(request, "home.html")


def show_car(request, car_id):
    try:
        car = Car.objects.get(id=car_id)
    except ObjectDoesNotExist:
        return JsonResponse({"error": "Sorry, the car not found."}, status=404)

    serializer = CarSerializer(car)
    return JsonResponse({"car": serializer.data}, status=200)

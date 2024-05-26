from django.db import models


class Car(models.Model):
    image1 = models.ImageField(upload_to="images", null=True, blank=True)
    image2 = models.ImageField(upload_to="images", null=True, blank=True)
    image3 = models.ImageField(upload_to="images", null=True, blank=True)
    image4 = models.ImageField(upload_to="images", null=True, blank=True)
    image5 = models.ImageField(upload_to="images", null=True, blank=True)
    image6 = models.ImageField(upload_to="images", null=True, blank=True)
    image7 = models.ImageField(upload_to="images", null=True, blank=True)
    image8 = models.ImageField(upload_to="images", null=True, blank=True)
    image9 = models.ImageField(upload_to="images", null=True, blank=True)
    registration_number = models.CharField(max_length=100)
    car_name = models.CharField(max_length=100)
    car_price = models.DecimalField(max_digits=10, decimal_places=2)
    car_description = models.TextField()
    part_exchange = models.BooleanField(default=False)
    car_mileage = models.DecimalField(max_digits=10, decimal_places=2)
    car_door = models.IntegerField()
    gear_box = models.CharField(max_length=100)
    engine_type = models.CharField(max_length=100)
    car_color = models.CharField(max_length=100)
    engine_position = models.CharField(max_length=100)
    aspiration = models.CharField(max_length=100)
    engine_size = models.CharField(max_length=100)
    cylinder_layout = models.CharField(max_length=100)
    fuel_consumption = models.CharField(max_length=100)
    health = models.CharField(max_length=100)
    cylinder = models.IntegerField()
    owners = models.IntegerField()
    top_speed = models.DecimalField(max_digits=10, decimal_places=2)
    driven_wheels = models.CharField(max_length=100)
    fname = models.CharField(max_length=100)
    lname = models.CharField(max_length=100)
    address1 = models.CharField(max_length=255)
    address2 = models.CharField(max_length=255)
    city = models.CharField(max_length=100)
    county = models.CharField(max_length=100)
    postcode = models.CharField(max_length=10)
    telephone_number = models.CharField(max_length=15)

    objects = models.Manager()

    def __str__(self):
        return f"{self.pk} {self.car_name}"

    class Meta:
        db_table = "car_registration"
        ordering = ["id"]

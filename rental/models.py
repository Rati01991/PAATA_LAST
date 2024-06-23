from django.db import models

class Car(models.Model):
    make = models.CharField(max_length=100)
    model = models.CharField(max_length=100)
    year = models.IntegerField()
    price_per_day = models.DecimalField(max_digits=8, decimal_places=2)
    available = models.BooleanField(default=True)
    image = models.ImageField(upload_to='cars/', default='cars/default_car.jpg')  # Specify upload_to and default image

    def __str__(self):
        return f"{self.year} {self.make} {self.model}"
    
    from django.db import models

class UserSubmittedCar(models.Model):
    make = models.CharField(max_length=100)
    model = models.CharField(max_length=100)
    year = models.IntegerField()
    price_per_day = models.DecimalField(max_digits=8, decimal_places=2)
    owner_name = models.CharField(max_length=100)
    owner_email = models.EmailField()
    description = models.TextField()

    def __str__(self):
        return f"{self.year} {self.make} {self.model} - {self.owner_email}"
    
class UserSubmittedCar(models.Model):
    make = models.CharField(max_length=100)
    model = models.CharField(max_length=100)
    year = models.IntegerField()
    price_per_day = models.DecimalField(max_digits=8, decimal_places=2)
    owner_name = models.CharField(max_length=100)
    owner_email = models.EmailField()
    description = models.TextField()

    # Add a foreign key to link to the User model for ownership
    owner = models.ForeignKey('auth.User', on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.year} {self.make} {self.model} - {self.owner_email}"
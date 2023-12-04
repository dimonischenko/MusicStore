from django.db import models

class Instrument(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    quantity = models.IntegerField()
    type_of_instrument = models.CharField(max_length=255)
    photo = models.ImageField()

    def __str__(self):
        return self.name

class Order(models.Model):
    product = models.ForeignKey(Instrument, on_delete=models.CASCADE)
    quantity = models.IntegerField()
    client_name = models.CharField(max_length=255)
    client_email = models.EmailField()
    date_of_order = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Order for {self.product.name} by {self.client_name}"
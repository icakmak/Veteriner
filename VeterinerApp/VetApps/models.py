from django.db import models

# Create your models here.
class Customer(models.Model):
    customerName = models.CharField(max_length=120)
    customerPhoto = models.CharField(max_length=120)
    customerAddress = models.CharField(max_length=250)
    customerCity = models.CharField(max_length=120)
    customerPhone = models.CharField(max_length=20)
    customerCreated = models.DateTimeField(auto_now_add=True)
    customerUpdated = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.customerName
    
class Kind(models.Model):
    kindName=models.CharField(max_length=50)
    kindCreated = models.DateTimeField(auto_now_add=True)
    kindUpdated = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.kindName 
    
class Animal(models.Model):
    animalCustomer=models.ForeignKey(Customer, on_delete=models.CASCADE, related_name='Animals')
    animalKind=models.ForeignKey(Kind, on_delete=models.CASCADE, related_name='Animals')
    animalName = models.CharField(max_length=120)
    animalPhoto = models.CharField(max_length=120)
    animalBirthdate = models.DateField()
    animalCreated = models.DateTimeField(auto_now_add=True)
    animalUpdated = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.animalName 


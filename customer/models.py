from django.db import models

# Model Tasks 1-5
#####################################

class Customer(models.Model):
      
    customer_name = models.CharField(max_length=100)

    def __str__(self):
        return self.customer_name
    
class Event(models.Model):
      
    event = models.CharField(max_length=100)

    def __str__(self):
        return self.event

######################################
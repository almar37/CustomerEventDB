from django.shortcuts import render
from .models import Customer, Event
from django.db import connection
from django.db.models import Q

# Part 2
#################################################################
def customer_list(request):

    posts = Customer.objects.all()

    print(posts)
    print(posts.query)
    print(connection.queries)
    

    return render(request, 'output.html',{'posts':posts})


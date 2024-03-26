from django.shortcuts import render, redirect
from models import Fact
facts = Fact.objects.all()
print(facts)
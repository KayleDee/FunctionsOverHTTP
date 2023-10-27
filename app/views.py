from django.shortcuts import render
from django.http.request import HttpRequest
from django.http.response import HttpResponse
# Create your views here.

def hey_you(request: HttpRequest, name: str) -> HttpResponse:
  return HttpResponse (f"Hey, {name.upper()}!")

def how_old (request: HttpRequest, end: int, birthyear: int) -> HttpResponse:
  return HttpResponse (end - birthyear)

def can_i_take_your_order(request: HttpRequest, burgers: int, fries: int, drinks: int) -> HttpResponse:
  total = burgers * 4.50 + fries * 1.50 + drinks * 1 
  return HttpResponse (total)
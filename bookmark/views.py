from django.shortcuts import render
from django.views.generic import ListView, DetailView

from .models import BookMark


class BookMarkListV(ListView):
    model = BookMark


class BookMarkDetailV(DetailView):
    model = BookMark








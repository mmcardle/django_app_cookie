from django.views.generic import DetailView, ListView, UpdateView, CreateView

from .models import {%for model in cookiecutter.models %}{{model}}{% if loop.index != loop.length %}, {%endif%}{%endfor%}
from .forms import {%for model in cookiecutter.models %}{{model}}Form{% if loop.index != loop.length %}, {%endif%}{%endfor%}

{%for model in cookiecutter.models %}

class {{ model }}ListView(ListView):
    model = {{ model }}


class {{ model }}CreateView(CreateView):
    model = {{ model }}
    form_class = {{ model }}Form


class {{ model }}DetailView(DetailView):
    model = {{ model }}


class {{ model }}UpdateView(UpdateView):
    model = {{ model }}
    form_class = {{ model }}Form

{%endfor%}
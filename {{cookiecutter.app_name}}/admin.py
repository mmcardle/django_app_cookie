from django.contrib import admin
from .models import {%for model in cookiecutter.models %}{{model}}{% if loop.index != loop.length %}, {%endif%}{%endfor%}
from .forms import {%for model in cookiecutter.models %}{{model}}Form{% if loop.index != loop.length %}, {%endif%}{%endfor%}

{% for model in cookiecutter.models %}

class {{ model }}Admin(admin.ModelAdmin):
    form = {{ model }}Form

admin.site.register({{ model }}, {{ model }}Admin)
{% endfor %}
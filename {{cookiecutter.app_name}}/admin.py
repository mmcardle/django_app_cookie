from django.contrib import admin
from django import forms
from .models import {%for model in cookiecutter.models %}{{model}}{% if loop.index != loop.length %}, {%endif%}{%endfor%}
from .forms import {%for model in cookiecutter.models %}{{model}}Form{% if loop.index != loop.length %}, {%endif%}{%endfor%}

{% for model in cookiecutter.models %}

class {{ model }}AdminForm(forms.ModelForm):

    class Meta:
        model = {{ model }}


class {{ model }}Admin(admin.ModelAdmin):
    form = {{ model }}AdminForm
    list_display = ['slug', 'created', 'last_updated']
    readonly_fields = ['slug', 'created', 'last_updated']

admin.site.register({{ model }}, {{ model }}Admin)
{% endfor %}
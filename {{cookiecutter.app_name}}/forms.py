__author__ = 'mm'

from django import forms
from .models import {%for model in cookiecutter.models %}{{model}}{% if loop.index != loop.length %}, {%endif%}{%endfor%}
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit

{%for model in cookiecutter.models %}
class {{ model }}Form(forms.ModelForm):
    class Meta:
        model = {{ model }}
        fields = ['name',]

    @property
    def helper(self):
        helper = FormHelper()
        helper.form_id = '{{model}}-form'
        helper.form_class = '{{model}}-form'
        helper.add_input(Submit('save', 'Save'))
        return helper
{%endfor%}
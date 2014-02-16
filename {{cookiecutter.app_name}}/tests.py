import unittest
from django.core.urlresolvers import reverse
from django.test import Client
from .models import {%for model in cookiecutter.models %}{{model}}{% if loop.index != loop.length %}, {%endif%}{%endfor%}
{%for model in cookiecutter.models %}


class {{ model }}ViewTest(unittest.TestCase):
    "Tests for model {{ model }}"
    def setUp(self):
        self.client = Client()

    def test_list_{{model}}(self):
        url = reverse('{{ cookiecutter.app_name }}_{{ model_name|lower }}_list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_create_{{model}}(self):
        data = {}
        url = reverse('{{ cookiecutter.app_name }}_{{ model_name|lower }}_create')
        response = self.client.post(url, data=data)
        self.assertEqual(response.status_code, 200)

    def test_detail_{{model}}(self):
        {{model|lower}} = {{model}}()
        {{model|lower}}.save()
        url = reverse('{{ cookiecutter.app_name }}_{{ model_name|lower }}_detail', args=[{{model|lower}}.slug, ])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_update_{{model}}(self):
        {{model|lower}} = {{model}}()
        {{model|lower}}.save()
        url = reverse('{{ cookiecutter.app_name }}_{{ model_name|lower }}_update', args=[{{model|lower}}.slug, ])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
{%endfor%}
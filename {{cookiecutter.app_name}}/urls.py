__author__ = 'mm'
{% set views = ['Detail', 'List', 'Create', 'Update'] %}
from django.conf.urls import patterns, url
{%for model in cookiecutter.models -%}
from .views import {%for view in views %}{{model}}{{view}}View{% if loop.index != loop.length %}, {%endif%}{%endfor%}
{%endfor%}

urlpatterns = patterns('{{ cookiecutter.app_name }}.views',
{%for model in cookiecutter.models %}
    # urls for {{model}}
    url(r'^{{model|lower}}/$', {{ model }}ListView.as_view(), name='{{ cookiecutter.app_name }}_{{ model|lower }}_list'),
    url(r'^{{model|lower}}/create/$', {{ model }}CreateView.as_view(), name='{{ cookiecutter.app_name }}_{{ model|lower }}_create'),
    url(r'^{{model|lower}}/(?P<slug>\S+)/update/$', {{ model }}UpdateView.as_view(), name='{{ cookiecutter.app_name }}_{{ model|lower }}_update'),
    url(r'^{{model|lower}}/(?P<slug>\S+)/$', {{ model }}DetailView.as_view(), name='{{ cookiecutter.app_name }}_{{ model|lower }}_detail'),
{%endfor%}
)
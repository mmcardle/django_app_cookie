#!/usr/bin/python
__author__ = 'mm'

import json
import os

print "Start Generate Templates Hook"

cookie_dir = '{{cookiecutter.app_name}}'
project_base = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
json_file = os.path.join(project_base, 'cookiecutter.json')
base_templates = os.path.join(project_base , 'base_templates')
cookie_templates = os.path.join(project_base, cookie_dir,
                                'templates', cookie_dir)

js = json.load(open(json_file, 'r'))

from jinja2 import FileSystemLoader
from jinja2.environment import Environment
from jinja2 import Template

env = Environment()
env.loader = FileSystemLoader(".")

for model in js['models']:
    for f in os.listdir(base_templates):
        basename = os.path.basename(f)
        cookie_filename = "%s_%s" % (model.lower(), basename)
        base_file = os.path.join(base_templates, f)
        cookie_file = os.path.join(cookie_templates, cookie_filename)

        ctx = js.copy()
        ctx.update({'model': model})

        _f_in = open(base_file, 'r')
        template = Template(_f_in.read())
        _f_in.close()

        output = template.render(**ctx)

        _f_out = open(cookie_file, 'wb')
        _f_out.write('{%% raw %%}%s{%% endraw %%}' % output)
        _f_out.close()
        print "Created Template %s" % cookie_file

print "End Generate Templates Hook"
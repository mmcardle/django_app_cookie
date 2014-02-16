#!/usr/bin/python
__author__ = 'mm'

import json
import os
import shutil

print "Start Generate Templates Hook"

cookie_dir = '{{cookiecutter.app_name}}'
project_base = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))

json_file = os.path.join(project_base, 'cookiecutter.json')
base_templates = os.path.join(project_base , 'base_templates')
cookie_templates = os.path.join(project_base, cookie_dir,
                                'templates', cookie_dir)

js = json.load(open(json_file, 'r'))

for model in js['models']:
    for f in os.listdir(base_templates):
        basename = os.path.basename(f)
        cookie_filename = "%s_%s" % (model.lower(), basename)
        base_file = os.path.join(base_templates, f)
        cookie_file = os.path.join(cookie_templates, cookie_filename)
        shutil.copy(base_file, cookie_file)
        print "Created Template %s" % cookie_file

print "End Generate Templates Hook"
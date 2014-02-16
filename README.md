Django App Cookies
=================

A [Cookie Cutter](https://github.com/audreyr/cookiecutter) to build a Django Application with multiple models.

Create Models, Views, Urls, Forms, Tests and Admin for each of the specified models.

Run
---------------
```
git clone https://github.com/mmcardle/django_app_cookie.git
cd django_app_cookie
vi cookiecutter.json 
cd <YOUR TARGET DIRECTORY>
cookiecutter <PATH TO django_app_cookie checkout>
```

Required Input
---------------
```
{
    "app_name": "test_app",
    "models": ["Model1", "Model2"]
}
```

Output Files
-------------

* models.py
* views.py
* urls.py
* admin.py
* forms.py
* tests.py 
* Templates for each Model
 * <Model>_list.html
 * <Model>_detail.html
 * <Model>_form.html


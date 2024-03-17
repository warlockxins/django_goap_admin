# Making initial setup - Admin
following steps of  https://docs.djangoproject.com/en/4.1/intro/tutorial01/

```bash
django-admin startproject goap_edit
```

created folder `goap_edit`
```
cd to goap_edit
python3.8 manage.py runserver
```

In same dir where manage.py is create a new app, [based on](https://docs.djangoproject.com/en/4.1/intro/tutorial01/#creating-the-polls-app):
```bash
python3.8 manage.py startapp goap
```

next create a view in `goap` https://docs.djangoproject.com/en/4.1/intro/tutorial01/#write-your-first-view

Complete urls section on https://docs.djangoproject.com/en/4.1/intro/tutorial01

# Models
based on https://docs.djangoproject.com/en/4.1/intro/tutorial02/
Add necessary classes in goap/models.py

then run:
```
python3.8 manage.py makemigrations goap
```

after done changes, apply by
```
python3.8 manage.py migrate
```

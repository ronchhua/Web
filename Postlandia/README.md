# Postlandia

A web application built using Django rest framework as the back-end, Vuejs as the front-end (CDN) with axios requests, and Bulma CSS framework.

## Overview

A simple web application that allows users to create posts on this website and display them on the homepage. This uses an api created by DRF to handle delete, get, and post requests to allow the user the functionality to create and delete posts. 


## Running on localhost

### Requirements
```bash
python -m pip install Django
pip install djangorestframework
pip install markdown
pip install django-filter
```

```bash
cd Postlandia/
python manage.py runserver
```

The base url, http://127.0.0.1:8000/, contains the main post page and http://127.0.0.1:8000/api/ displays the extensions of URLS to view the api.

# adaptwms
Lightweight OpenStreetMap adapter for WMS services

## What it is?

Basically it is adapter translating requests in so called
[Slippy Map format](https://wiki.openstreetmap.org/wiki/Slippy_map) (used by
OpenStreetMap, takes zoom level and XY tile indexes) into requests to external
WMS service (takes bounding box in form of two points in some coordinate
system of area to render).

To give an example , let's say you need to supply to external map viewer an URL in format:

```
https://tile.openstreetmap.org/{z}/{x}/{y}.png
```

All x,y and z are natural numbers. But the service you want to access gives you interface that requires this format:

```
https://external.service/wms?BBOX=0.0%2C0.0%2C1.0%2C1.0&SRS=EPSG%3A3857&WIDTH=256&HEIGHT=256&SERVICE=WMS
```

However in this case BBOX contains set of 4 floating point numbers for 2 (x<sub>0</sub>, y<sub>0</sub>) and (x<sub>1</sub>, y<sub>1</sub>) points limiting the area to render. This is a kind of problems this program is trying to solve.

## What is supported?

These are the known constraints:
- WMS service you use must allow unauthenticated access (there is no way for passing credentials in any form at the moment)
- it must support **EPSG:3857** coordinate system

## How to use it...

### ...if I don't have experience with Django

This makes use of this Github project and demo project it supplies. Best for testing, or temporary deployement.

1. Make sure you have Python and pip installed
2. Clone repo: `git clone git@github.com:v3l0c1r4pt0r/adaptwms.git` and enter it: `cd adaptwms`
3. Install all requirements: `pip install -r requirements.txt`
4. Run development server with: `./manage.py runserver`
5. Open `http://127.0.0.1:8000/` in your browser

**TODO**: write

### ...if I do have some experience with Django

This makes use of pip package available on PyPI and Django project that you have, or want to set up. Best for production environments.

1. Make sure you have Python and pip installed
2. Start new django project: `django-admin startproject demo .`, where demo is its name, or use existing one
3. Install adaptwms from PyPI: `pip install adaptwms`
4. Add `adaptwms` to your `INSTALLED_APPS` in settings.py
5. Add `path("adaptwms/", adaptwms.views.adapter_view),` to your urlpatterns in urls.py
6. Run development server with: `./manage.py runserver`
7. Open `http://127.0.0.1:8000/` in your browser

# ZuriMart

A Django-based marketplace website with home, about, products, services, and contact pages.

## Run locally on Linux

```bash
python3 -m venv shop
source shop/bin/activate
python3 -m pip install Django==6.1.2
export DJANGO_SECRET_KEY="$(python3 -c 'from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())')"
python3 manage.py runserver
```

Open http://127.0.0.1:8000/index/ in your browser.

# Cara setup Django Project

1. Buat project
  - `django-admin startproject mywebsite`
2. Buat app
  - `cd mywebsite`
  - `python manage.py startapp <nama-app>`
3. Atur templating
  - Dari root project, buka settings.py di `mywebsite`
  - Cari TEMPLATES.DIRS, lalu isikan dengan `'templates'`
  - Buat folder `templates` di root project
4. Atur index project dan setting routing
  - Buka `urls.py` di project `mywebsite`
    - Dibaris import, ubah menjadi: `from django.urls import path, include`
    - Tambahkan `from . import views`
    - Di `urlpatterns`, tambahkan `path('', views.index)`
  - Buat file `views.py` di project `mywebsite`
    - Atur views
      - Gunakan `django.http.HttpResponse()`
      - Atau `django.shortcuts.render()`
        - Dengan template HTML di folder `templates`
5. Atur app routing dan app views
  - Buka `urls.py` di project `mywebsite`
    - Di `urlpatterns`, tambahkan `path('<nama-app>/', include('<nama-app>.urls'))`
  - Buat file `urls.py` di dalam folder `<nama-app>`
    - Isikan dengan:
      - Path import: `from django.urls import path`
      - Daftar routing: `urlpatterns = []`
  - Buka file `views.py` di project `mywebsite`
    - Atur views

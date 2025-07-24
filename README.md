##Paso a paso para trabajar en Django

📁 1. Crear y activar el entorno virtual
python -m venv entorno
source entorno/bin/activate       # Linux / macOS
entorno\Scripts\activate          # Windows
⬇️ 2. Instalar Django y dependencias
pip install django

# En caso de usar un archivo requirements.txt
pip install -r requirements.txt
📂 3. Crear archivo `.gitignore` (opcional)
env/
__pycache__/
*.pyc
db.sqlite3
🏗️ 4. Crear el proyecto Django
django-admin startproject proyecto
cd proyecto
⚙️ 5. Crear una aplicación
python manage.py startapp web
⚙️ 6. Registrar la app en el archivo `settings.py`
INSTALLED_APPS = [
    ..., 
    'web',
]
🌐 7. Configurar rutas (URLs)
7.1 En `web/urls.py`:
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
]

7.2 En `proyecto/urls.py`:
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('web.urls')),
]
🧠 8. Crear la vista principal en `web/views.py`
from django.shortcuts import render

def home(request):
    return render(request, "base.html")
🧱 9. Crear estructura de templates
Opción A: Templates dentro de la app
web/templates/web/base.html → render(request, "web/base.html")

Opción B: Templates globales
templates/base.html → render(request, "base.html")

Y en `settings.py`:
TEMPLATES = [
    {
        'DIRS': [BASE_DIR / "templates"],
        'APP_DIRS': True,
    },
]
🛠️ 10. Preparar y aplicar migraciones
python manage.py makemigrations
python manage.py migrate
👤 11. Crear usuario administrador (opcional)
python manage.py createsuperuser
🚀 12. Ejecutar el servidor
python manage.py runserver

Luego visitar:
http://localhost:8000/

🔐 13. Configurar seguridad para desarrollo en `settings.py`
ALLOWED_HOSTS = ['localhost', '127.0.0.1']

CSRF_TRUSTED_ORIGINS = [
    "https://localhost:8000",
]

python -m venv djangoIA
.\Scripts\activate
pip install django==3.1
django-admin startproject ia_cloud
python manage.py runserver
python manage.py migrate

launch project =>
python manage.py startapp app_project

creatation d'une app =>
python manage.py startapp app_project

Préparation du fichier de modification de la base =>
python manage.py makemigrations

Commande pour pousser le
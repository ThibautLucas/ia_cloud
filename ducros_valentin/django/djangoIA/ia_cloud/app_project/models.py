from django.db import models
from django.contrib.auth.models import User

# Créer modèles Profile
# Champs : user (OnetoOne), firstname (Charfield), lastname(Charfield), location(Charfield), creation_date(DateTimeField)
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True,)
    firstname = models.CharField(max_length=30)
    lastname = models.CharField(max_length=30)
    location = models.CharField(max_length=30)
    creation_date = models.DateTimeField(auto_now_add=True)

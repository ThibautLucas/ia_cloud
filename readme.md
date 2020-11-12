<<<<<<< Updated upstream
## Projet IA dans le cloud

1. Détecteur de visage :
    - Entrée = nom du fichier
    - Sortie = Image avec visage entourée + Coordonnées des prédictions

2. Serveur Flask :
    - Installez Flask dans votre environnement
    - Créer un serveur de base https://flask.palletsprojects.com/en/1.1.x/quickstart/
    - Créer une route d'API (/predict) faisant appel à votre fonction de détection de visage (qui doit cette fois uniquement retourner les prédictions, pas afficher l'image)
    - Retournez un JSON avec la liste des prédictions

3. Jupyter:
    - Faire un appel d'API dans un notebook vers votre serveur Flask en envoyant un JSON contenant le path vers l'image où faire les détections
    - Récupérer les coordonnées des prédictions renvoyées par votre API
    - Avec OpenCV tracez ces prédictions sur l'image que vous aurez chargée dans le notebook et afficher le résultat
=======
##Projet IA dans le cloud
>>>>>>> Stashed changes

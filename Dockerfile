# Utiliser une image Python officielle comme base
FROM python:3.9-slim

# Définir le répertoire de travail dans le conteneur
WORKDIR /app

# Copier le fichier requirements.txt dans le conteneur
COPY requirements.txt /app/

# Installer les dépendances
RUN pip install --no-cache-dir -r requirements.txt

# Copier l'intégralité du projet dans le conteneur
COPY . /app/

# Exposer le port que l'application va utiliser
EXPOSE 8000

# Définir la commande de démarrage par défaut
CMD ["gunicorn", "--bind", "0.0.0.0:8000", "myproject.wsgi:application"]

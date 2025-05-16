# Image officielle Python
FROM python:3.12-slim

# Définir le dossier de travail
WORKDIR /app

# Copier les fichiers du projet
COPY . .

# Installer les dépendances
RUN pip install --no-cache-dir -r requirements.txt

# Collecter les fichiers statiques (optionnel si tu as des fichiers statiques)
RUN python manage.py collectstatic --noinput

# Exposer le port 8000
EXPOSE 8000

# Commande pour lancer Gunicorn (serveur WSGI de production)
CMD ["gunicorn", "olympic_tickets.wsgi:application", "--bind", "0.0.0.0:8000"]

# Utilise Python officiel (léger)
FROM python:3.10-slim

# Définir le répertoire de travail
WORKDIR /app

# Copier tout le projet dans le conteneur
COPY . .

# Installer les dépendances
RUN pip install --upgrade pip && pip install -r requirements.txt

# Collecte les fichiers statiques
RUN python manage.py collectstatic --noinput || true

# Exposer le port
EXPOSE 8000

# Lancer Gunicorn pour servir l'application Django
CMD ["gunicorn", "olympic_tickets.wsgi:application", "--bind", "0.0.0.0:8000"]

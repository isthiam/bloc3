# 🎟️ Application de Réservation de e-Tickets – JO 2024

## 🚀 Description

Cette application Django permet aux utilisateurs de consulter et réserver des billets pour les Jeux Olympiques 2024. Elle intègre un espace administrateur complet, un système de panier, une validation de paiement, un système de QR code pour la validation des billets, ainsi que des statistiques de ventes.

---

## 🧩 Fonctionnalités principales

- 🔐 Authentification et gestion de profil utilisateur
- 🎫 Réservation de billets (Solo, Duo, Famille)
- 🛒 Gestion du panier et validation du paiement
- 📈 Statistiques des ventes (admin)
- 🧾 Génération de billets PDF avec QR Code
- ✅ Validation de billets via scan (admin)
- 📩 Formulaire de contact
- 🌍 Déploiement Fly.io

---

## 🏗️ Stack Technique

- **Back-end :** Django 5.x
- **Base de données :** PostgreSQL
- **Génération PDF :** WeasyPrint / ReportLab
- **Frontend :** HTML/CSS + Bootstrap
- **Déploiement :** Docker + Fly.io

---

## ⚙️ Installation locale

1. **Cloner le dépôt**
   ```bash
   git clone https://github.com/ton-compte/jo2024-etickets.git
   cd jo2024-etickets
<<<<<<< HEAD
   ```

2. **Créer un environnement virtuel**
   ```bash
   python -m venv env
   source env/bin/activate  # Linux/macOS
   env\Scripts\activate     # Windows
   ```

3. **Installer les dépendances**
   ```bash
   pip install -r requirements.txt
   ```

4. **Créer la base de données**
   ```bash
   python manage.py migrate
   ```

5. **Créer un superutilisateur**
   ```bash
   python manage.py createsuperuser
   ```

6. **Lancer le serveur local**
   ```bash
   python manage.py runserver
   ```

---

## 🧪 Tests

```bash
python manage.py test
```

> ✅ Couverture test visée : 90% – Tests passant : 95%

---

## 📦 Déploiement (Fly.io)

```bash
fly launch
fly deploy
```

---

## 📁 Structure des dossiers

```
📁 olympic_tickets/
├── users/              → gestion des utilisateurs
├── offres/             → gestion des offres de billets
├── tickets/            → gestion des réservations et QR codes
├── contact/            → formulaire de contact
├── templates/          → templates HTML
├── static/             → fichiers statiques (logos, styles)
├── media/              → fichiers PDF générés
```

---

## 📄 Licence

Ce projet est développé dans le cadre de la formation **Bloc 3 – Studi**. Pour usage éducatif uniquement.

---

## ✍️ Auteur

Issakha Thiam – [LinkedIn](https://www.linkedin.com) – Data Manager & Développeur Python
=======
>>>>>>> ebea5e5c705b29bf35eadaebd2cb5b1adc562421

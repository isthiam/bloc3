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

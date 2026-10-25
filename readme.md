# Green Move Logistics — Refactoring IoT & Industrialisation (Bloc 3)

**Candidat :** MOHAMED MOIBIOI  
**Rôle :** Chief Technical Officer (CTO)  
**Entreprise :** Green Move Logistics  
**Projet :** Industrialisation de la solution embarquée sur 5 000 camions (Horizon 4 mois)

---

## 📌 Description du Projet

Ce dépôt contient le code refactorisé de l'application IoT embarquée sur les tablettes Zebra de la flotte Green Move Logistics. Il résout les problèmes majeurs identifiés lors du pilote (fuites mémoire RAM, blocages I/O en zone 4G faible) et pose les bases d'un déploiement OTA sécurisé.

### Correctifs apportés par rapport au POC initial (`poc.py`) :
1. **Élimination de la fuite mémoire (OOM Killer) :** Remplacement du tampon de liste globale par une file d'attente `asyncio.Queue` bornée (max 1 000 éléments) maintenant l'empreinte RAM sous les 25 Mo.
2. **Gestion Asynchrone (I/O non-bloquant) :** Utilisation de `asyncio` et `aiohttp` pour séparer la collecte de données capteurs de l'envoi réseau HTTP.
3. **Persistance en mode déconnecté (Zone blanche 4G) :** En cas d'échec réseau, stockage local automatique des alertes dans une base de données embarquée **SQLite**.
4. **Sécurisation :** Suppression des tokens inscrits en dur dans le code source au profit de variables sécurisées.

---

## 🛠️ Stack Technique

* **Langage :** Python 3.10+
* **Framework Asynchrone :** `asyncio`, `aiohttp`
* **Base de données embarquée :** SQLite 3
* **Tests unitaires :** `unittest`, `unittest.mock`

---

## 📂 Structure du Dépôt
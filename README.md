# LLM_MASCIR
# Assistant Vocal Intégré avec Gestion de Réunions et Divertissement

## Introduction

### Description du Projet

Ce projet est une application complète intégrant un assistant vocal utilisant l'API GPT-4, capable de gérer les rendez-vous Google Meet, les préférences musicales des utilisateurs, ainsi que les interactions avec une base de données PostgreSQL. L'application permet également de rechercher et de lire des vidéos YouTube directement via l'assistant vocal. Ce projet est conçu pour être utilisé dans des environnements tels que des maisons de retraite où les utilisateurs peuvent bénéficier d'un assistant vocal pour la gestion de leur santé, de leurs rendez-vous et de leur divertissement.

### Objectif

L'objectif principal de ce projet est de fournir un assistant vocal complet et intégré qui :

- Permet la création et la gestion de réunions Google Meet.
- Envoie automatiquement les invitations par e-mail avec les liens des réunions.
- Gère les préférences musicales des utilisateurs et suggère des vidéos YouTube en fonction de ces préférences.
- Utilise des API externes pour l'accès aux services de Google et YouTube, ainsi qu'une base de données PostgreSQL pour stocker et gérer les informations des utilisateurs.
- Offre une interface conviviale pour les utilisateurs, avec des fonctionnalités de reconnaissance vocale et de génération de texte à partir de la voix.

Ce projet est destiné à améliorer l'expérience des utilisateurs en leur offrant une solution technologique avancée et facile à utiliser pour la gestion de leur santé et de leur divertissement.


## Prérequis

### Environnement de Développement

Pour développer et exécuter ce projet, vous devez configurer votre environnement de développement avec les outils et bibliothèques nécessaires. Voici les étapes à suivre :

1. **Installer Python** : Assurez-vous d'avoir Python 3.7 ou une version ultérieure installée sur votre machine. Vous pouvez télécharger Python depuis [python.org](https://www.python.org/downloads/).

2. **Créer un Environnement Virtuel** : Il est recommandé de créer un environnement virtuel pour gérer les dépendances du projet. Voici comment le faire :
   
   ```bash
   python -m venv env
Activez l'environnement virtuel :

Sur Windows :
bash
Copier le code
.\env\Scripts\activate
Sur macOS/Linux :
bash
Copier le code
source env/bin/activate
Installer les Dépendances : Une fois l'environnement virtuel activé, installez les dépendances nécessaires en utilisant le fichier requirements.txt. Exécutez la commande suivante :

bash
Copier le code
pip install -r requirements.txt
Applications Nécessaires
Certaines applications et outils doivent être installés pour le bon fonctionnement de ce projet :

Navigateurs Web : Pour les fonctionnalités liées aux API Google, un navigateur web est nécessaire pour l'authentification OAuth.

Client de Messagerie : Assurez-vous d'avoir un client de messagerie pour tester l'envoi d'e-mails via SMTP. Le projet utilise le serveur SMTP de Gmail, donc un compte Gmail est recommandé.

Lecteur de Vidéos : Pour visualiser les vidéos YouTube téléchargées, installez VLC Media Player, qui est utilisé pour lire les vidéos téléchargées par yt_dlp.

Google Chrome ou Chromium : Pour l'authentification OAuth, un navigateur moderne comme Google Chrome ou Chromium est recommandé pour faciliter le processus de connexion et d'autorisation.




## Configuration de l'Environnement

### Création d'un Environnement Virtuel

Pour garantir que les dépendances de votre projet ne conflit pas avec celles d'autres projets, il est recommandé de créer un environnement virtuel. Voici les étapes pour le faire :

1. **Créer l'Environnement Virtuel** : Exécutez la commande suivante dans le terminal à la racine de votre projet :

   ```bash
   python -m venv env

Activer l'Environnement Virtuel :

Sur Windows :
bash
Copier le code
.\env\Scripts\activate
Sur macOS/Linux :
bash
Copier le code
source env/bin/activate
Vous devriez voir le nom de votre environnement virtuel (par exemple, (env)) au début de la ligne de commande, ce qui indique que l'environnement virtuel est activé.

Installation des Dépendances
Une fois l'environnement virtuel activé, vous devez installer toutes les dépendances nécessaires pour faire fonctionner le projet. Ces dépendances sont listées dans le fichier requirements.txt. Voici comment procéder :

Installer les Dépendances : Exécutez la commande suivante pour installer toutes les dépendances à partir du fichier requirements.txt :

bash
Copier le code
pip install -r requirements.txt
Cette commande téléchargera et installera toutes les bibliothèques et outils nécessaires à partir de PyPI (Python Package Index).

Vérifier les Dépendances : Après l'installation, vous pouvez vérifier que toutes les dépendances sont correctement installées en exécutant :

bash
Copier le code
pip list
Cette commande affichera la liste des packages installés dans votre environnement virtuel.




## Obtention des Clés API

### Configuration de l'API Google

Pour accéder aux services Google tels que Google Calendar et Google Meet, vous devez configurer l'API Google et obtenir les informations d'authentification nécessaires.

1. **Accéder à la Google Cloud Console** :
   - Rendez-vous sur la [Google Cloud Console](https://console.cloud.google.com/).

2. **Créer un Projet** :
   - Cliquez sur le sélecteur de projet en haut de la page, puis sur "Nouveau projet".
   - Donnez un nom à votre projet et cliquez sur "Créer".

3. **Activer les APIs** :
   - Dans le menu de la console, allez dans "API et services" > "Bibliothèque".
   - Recherchez et activez l'API "Google Calendar API".

4. **Configurer les Identifiants** :
   - Allez dans "API et services" > "Identifiants".
   - Cliquez sur "Créer des identifiants" et sélectionnez "ID client OAuth".
   - Choisissez "Application de bureau" comme type d'application.
   - Donnez un nom à vos identifiants et cliquez sur "Créer".

5. **Télécharger le Fichier `credentials.json`** :
   - Après avoir créé les identifiants, vous verrez un bouton "Télécharger" à côté de votre nouvel ID client OAuth.
   - Téléchargez ce fichier JSON et placez-le dans le répertoire racine de votre projet sous le nom `credentials.json`.

### Configuration de l'API YouTube

Pour intégrer des fonctionnalités de YouTube, telles que la recherche et la lecture de vidéos, vous devez configurer l'API YouTube.

1. **Accéder à la Google Cloud Console** :
   - Utilisez le même projet que précédemment ou créez-en un nouveau si nécessaire.

2. **Activer l'API YouTube Data** :
   - Dans le menu de la console, allez dans "API et services" > "Bibliothèque".
   - Recherchez et activez l'API "YouTube Data API v3".

3. **Créer une Clé API** :
   - Allez dans "API et services" > "Identifiants".
   - Cliquez sur "Créer des identifiants" et sélectionnez "Clé API".
   - Copiez la clé API générée. Vous en aurez besoin pour interagir avec l'API YouTube.

### Obtention de la Clé API YouTube

1. **Copier la Clé API** :
   - Conservez la clé API YouTube que vous avez générée dans la section précédente. Vous l'utiliserez dans votre application pour authentifier vos requêtes à l'API YouTube.

2. **Configurer l'API YouTube dans votre Application** :
   - Assurez-vous de stocker votre clé API de manière sécurisée dans votre environnement de développement, par exemple en utilisant des variables d'environnement.

Avec ces étapes complètes, vous serez prêt à intégrer les services Google et YouTube dans votre projet. Assurez-vous de suivre les instructions suivantes pour configurer la base de données PostgreSQL et intégrer les fonctionnalités de votre application.



## Configuration de la Base de Données PostgreSQL

### Installation de PostgreSQL

1. **Télécharger PostgreSQL** :
   - Rendez-vous sur le site officiel de PostgreSQL à l'adresse [https://www.postgresql.org/download/](https://www.postgresql.org/download/).
   - Sélectionnez votre système d'exploitation et suivez les instructions pour télécharger et installer PostgreSQL.

2. **Installer PostgreSQL** :
   - Suivez les instructions d'installation fournies pour votre système d'exploitation.
   - Pendant l'installation, vous serez invité à définir un mot de passe pour l'utilisateur `postgres`. Notez ce mot de passe, car vous en aurez besoin pour accéder à PostgreSQL.

3. **Vérifier l'Installation** :
   - Après l'installation, ouvrez un terminal (ou l'invite de commande) et tapez `psql --version` pour vérifier que PostgreSQL est correctement installé.

### Création de la Base de Données

1. **Accéder au Terminal PostgreSQL** :
   - Ouvrez un terminal et connectez-vous à PostgreSQL avec la commande suivante :
     ```bash
     psql -U postgres
     ```
   - Entrez le mot de passe que vous avez défini pendant l'installation.

2. **Créer une Nouvelle Base de Données** :
   - Dans le terminal PostgreSQL, créez une nouvelle base de données en utilisant la commande suivante :
     ```sql
     CREATE DATABASE mydatabase;
     ```
   - Remplacez `mydatabase` par le nom que vous souhaitez donner à votre base de données.

3. **Quitter le Terminal PostgreSQL** :
   - Tapez `\q` pour quitter le terminal PostgreSQL.

### Commandes SQL pour la Création des Tables

1. **Accéder à la Nouvelle Base de Données** :
   - Connectez-vous à la base de données que vous avez créée avec la commande suivante :
     ```bash
     psql -U postgres -d mydatabase
     ```

2. **Créer les Tables** :
   - Exécutez les commandes SQL suivantes pour créer les tables nécessaires dans votre base de données. Modifiez les noms des tables et des colonnes en fonction de vos besoins spécifiques :

   ```sql
   -- Table pour stocker les informations des utilisateurs
   CREATE TABLE users (
       id SERIAL PRIMARY KEY,
       first_name VARCHAR(50) NOT NULL,
       last_name VARCHAR(50) NOT NULL,
       room_number VARCHAR(10),
       email VARCHAR(100) UNIQUE NOT NULL
   );

   -- Table pour stocker les informations de santé
   CREATE TABLE health_info (
       id SERIAL PRIMARY KEY,
       user_id INTEGER REFERENCES users(id),
       health_status TEXT,
       last_update TIMESTAMP DEFAULT CURRENT_TIMESTAMP
   );

   -- Table pour stocker les informations sur les médicaments
   CREATE TABLE medications (
       id SERIAL PRIMARY KEY,
       user_id INTEGER REFERENCES users(id),
       medication_name VARCHAR(100),
       dosage TEXT,
       schedule TEXT
   );

   -- Table pour stocker les préférences de divertissement
   CREATE TABLE entertainment_info (
       id SERIAL PRIMARY KEY,
       user_id INTEGER REFERENCES users(id),
       favorite_genres TEXT[],
       preferred_artists TEXT[]
   );

   -- Table pour stocker les préférences musicales
   CREATE TABLE music_preferences (
       id SERIAL PRIMARY KEY,
       user_id INTEGER REFERENCES users(id),
       preferred_genres TEXT[],
       favorite_artists TEXT[]
   );




## Téléchargement des Applications Nécessaires

### Installation de VLC

VLC Media Player est nécessaire pour lire les vidéos YouTube téléchargées par votre application. Voici comment l'installer :

- **Windows** :
  1. Rendez-vous sur le site officiel de VLC [VLC Media Player](https://www.videolan.org/vlc/).
  2. Téléchargez l'installateur pour Windows.
  3. Exécutez le fichier téléchargé et suivez les instructions pour installer VLC.

- **macOS** :
  1. Rendez-vous sur le site officiel de VLC [VLC Media Player](https://www.videolan.org/vlc/).
  2. Téléchargez le fichier DMG pour macOS.
  3. Ouvrez le fichier DMG et faites glisser l'icône VLC dans le dossier Applications.

- **Linux** :
  1. Ouvrez un terminal.
  2. Utilisez la commande suivante pour installer VLC :
     ```bash
     sudo apt-get update
     sudo apt-get install vlc
     ```

### Installation de Python et des Bibliothèques Requises

Assurez-vous que Python est installé sur votre système. Vous pouvez télécharger Python depuis [python.org](https://www.python.org/downloads/). Une fois Python installé, procédez comme suit :

Une fois que tout est configuré et que les dépendances sont installées, suivez les étapes ci-dessous pour exécuter le code :

1. **Activer l'Environnement Virtuel** :
   Avant de lancer le code, assurez-vous que l'environnement virtuel est activé.
   - **Windows** :
     ```bash
     venv\Scripts\activate
     ```
   - **macOS/Linux** :
     ```bash
     source venv/bin/activate
     ```

2. **Exécuter le Script Principal** :
   Lancez le script principal `llm.py` qui gère toutes les fonctionnalités de l'application, y compris la création de réunions Google Meet, l'envoi d'e-mails, l'interaction avec YouTube, et la gestion de la base de données PostgreSQL :
   ```bash
   python llm.py
Suivre les Instructions à l'Écran :
Le script vous guidera à travers les différentes étapes, telles que :
Vérification de l'utilisateur dans la base de données.
Saisie des informations de santé et de médication.
Planification de réunions Google Meet.
Lecture de vidéos YouTube en fonction des préférences de l'utilisateur.

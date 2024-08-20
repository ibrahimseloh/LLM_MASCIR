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

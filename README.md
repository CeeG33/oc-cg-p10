- ![Static Badge](https://img.shields.io/badge/P10_Creez_une_API_s%C3%A9curis%C3%A9e_RESTful_en_utilisant_Django_REST-blue?label=Projet)
- ![Static Badge](https://img.shields.io/badge/Ciran_G%C3%9CRB%C3%9CZ-darkgreen?label=Auteur)
- ![Static Badge](https://img.shields.io/badge/Ao%C3%BBt_2023-yellow?label=Date)
- ![Static Badge](https://img.shields.io/badge/Python-blue?label=Language) [![Code style: black](https://img.shields.io/badge/Code%20style-Black-000000.svg)](https://github.com/psf/black)


# SoftDesk Support API: API de gestion de problèmes techniques (English version down below)

SoftDesk Support API est une application web à éxecuter localement. Il s'agit d'un outil permettant permettant de remonter et suivre des problèmes techniques. Cette application est implémentée sous la forme d'une API REST. Elle permet la lecture et la création d'utilisateurs et de projets contenant des tickets et des commentaires. Ces actions sont possibles à partir d'URLs interrogeables à l'aide de Postman. Les points d'entrées fournis par cette API et les requêtes réalisables sont détaillés dans les sections suivantes.

## Installation

Cette API exécutable localement peut être installée en suivant les étapes décrites ci-dessous. L'usage de Poetry est recommandé, mais des instuctions utilisant venv et pip sont également fournies plus bas. Si Poetry n'est pas encore installé sur votre ordinateur, vous trouverez des instuctions d'installation détaillées [sur cette page](https://python-poetry.org/docs/basic-usage/).

### Installation et exécution de l'application avec Poetry

1. Clonez ce dépôt de code à l'aide de la commande `$ git clone https://github.com/CeeG33/oc-cg-p10` (vous pouvez également télécharger le code [en tant qu'archive zip](https://github.com/CeeG33/oc-cg-p10/archive/refs/heads/main.zip))
2. Rendez vous depuis un terminal à la racine du répertoire oc-cg-p10 avec la commande `$ cd oc-cg-p10`
3. Installez les dépendances du projet à l'aide de la commande `$ poetry install` 
4. Démarrez le serveur avec `$ poetry run python manage.py runserver`

Lorsque le serveur fonctionne (après l'étape 4 de la procédure), l'API SoftDesk Support peut être interrogée à partir des points d'entrée commençant par l'URL de base [http://127.0.0.1:8000/api/](http://127.0.0.1:8000/api/). 

Les étapes 1 à 3 ne sont requises que pour l'installation initiale. Pour les lancements ultérieurs du serveur de l'API, il suffit d'exécuter l'étape 4 à partir du répertoire racine du projet.

### Installation et exécution de l'application sans Poetry (avec venv et pip)

1. Clonez ce dépôt de code à l'aide de la commande `$ git clone https://github.com/CeeG33/oc-cg-p10` (vous pouvez également télécharger le code [en tant qu'archive zip](https://github.com/CeeG33/oc-cg-p10/archive/refs/heads/main.zip))
2. Rendez vous depuis un terminal à la racine du répertoire oc-cg-p10 avec la commande `$ cd oc-cg-p10`
3. Créez un environnement virtuel pour le projet avec `$ python -m venv env` sous Windows ou `$ python3 -m venv env` sous MacOS ou Linux.
4. Activez l'environnement virtuel avec `$ env\Scripts\activate` sous Windows ou `$ source env/bin/activate` sous MacOS ou Linux.
5. Installez les dépendances du projet avec la commande `$ pip install -r requirements.txt`
6. Démarrez le serveur avec `$ python manage.py runserver`

Lorsque le serveur fonctionne (après l'étape 4 de la procédure), l'API SoftDesk Support peut être interrogée à partir des points d'entrée commençant par l'URL de base [http://127.0.0.1:8000/api/](http://127.0.0.1:8000/api/). 

Les étapes 1 à 3 ne sont requises que pour l'installation initiale. Pour les lancements ultérieurs du serveur de l'API, il suffit d'exécuter les étapes 4 à 6 à partir du répertoire racine du projet.

## Comptes pré-existants

Voici une liste d'utilisateurs créés à titre d'illustration :

```
Login : admin - MDP : admin << Compte administrateur
Login : Maxime - MDP : maxime
Login : Pierre - MDP : pierre
Login : Julie - MDP : julie
Login : Célia - MDP : celia
```


## Utilisation et documentation des points d'entrée

L'API fournit les points d'entrées suivants: 

| Endpoints  | Requêtes autorisés | Pré-requis | Utilisations |
| :---:        | :---:                | :---         | :---           |
| api/token/ | POST      | S'identifier avec un compte pré-existant | Obtenir un token pour accéder à l'API |
| api/<br>user/  | GET, POST | Être authentifié                         | Visualiser la liste des utilisateurs ou créer un nouvel utilisateur |
| api/<br>user/<br><user_pk>/ | GET, PUT, PATCH, DELETE | Lecture : être authentifié; Modification : Seul l'utilisateur en question peut modifier ou supprimer ses données | Visualiser ou modifier/supprimer les détails d'un utilisateur. Note : seuls les pages des utilisateurs ayant accepté de partager leurs données peuvent être visualisées |
| api/<br>project/ | GET, POST | Être authentifié | Visualiser la liste des projets ou créer un nouveau projet. Note : seuls les projets où l'utilisateur est contributeur seront affichés |
| api/<br>project/<br><project_pk>/ | GET, PUT, PATCH, DELETE | Lecture : être authentifié et contributeur du projet; Modification : être l'auteur du projet | Visualiser ou modifier/supprimer les détails d'un projet |
| api/<br>project/<br><project_pk>/<br>issue/ | GET, POST | Être authentifié et contributeur du projet | Visualiser la liste des tickets ou créer un nouveau ticket sur un projet donné. Note : seuls les tickets du projet sélectionné seront affichés |
| api/<br>project/<br><project_pk>/<br>issue/<br><issue_pk> | GET, PUT, PATCH, DELETE | Lecture : être authentifié et contributeur du projet; Modification : être l'auteur du ticket | Visualiser ou modifier/supprimer les détails d'un ticket |
| api/<br>project/<br><project_pk>/<br>issue/<br><issue_pk>/<br>comment/ | GET, POST | Être authentifié et contributeur du projet | Visualiser la liste des commentaires ou créer un nouveau commentaire sur un ticket donné. Note : seuls les commentaires du ticket sélectionné seront affichés |
| api/<br>project/<br><project_pk>/<br>issue/<br><issue_pk>/<br>comment/<br><comment_pk>/ | GET, PUT, PATCH, DELETE | Lecture : être authentifié et contributeur du projet; Modification : être l'auteur du commentaire | Visualiser ou modifier/supprimer les détails d'un commentaire |

La documentation Postman des endpoints est également visible en suivant [ce lien](https://documenter.getpostman.com/view/29348288/2s9YBxZwPn#intro).


__________________________________________


# SoftDesk Support API: Technical Issue Management API

The SoftDesk Support API is a web application that can be run locally. It is a tool for reporting and tracking technical issues. This application is implemented as a REST API. It allows reading and creating users and projects that contain tickets and comments. These actions can be performed using Postman to query URLs. The entry points provided by this API and the requests that can be made are detailed in the following sections.

## Installation

This locally executable API can be installed by following the steps described below. Poetry usage is recommended, but instructions using venv and pip are also provided below. If Poetry is not already installed on your computer, you can find detailed installation instructions [on this page](https://python-poetry.org/docs/basic-usage/).

### Installation and Running the Application with Poetry

1. Clone this code repository using the command `$ git clone https://github.com/CeeG33/oc-cg-p10` (you can also download the code as a [ZIP archive](https://github.com/CeeG33/oc-cg-p10/archive/refs/heads/main.zip)
2. Navigate to the root directory of the oc-cg-p10 repository using a terminal with the command `$ cd oc-cg-p10`
3. Install project dependencies using the command `$ poetry install` 
4. Start the server with `$ poetry run python manage.py runserver`

When the server is running (after step 4 of the procedure), the SoftDesk Support API can be queried from the entry points starting with the base URL [http://127.0.0.1:8000/api/](http://127.0.0.1:8000/api/). 

Steps 1 to 3 are only required for the initial installation. For subsequent launches of the API server, simply execute step 4 from the project's root directory.

### Installation and running the application without Poetry (using venv and pip)

1. Clone this code repository using the command `$ git clone https://github.com/CeeG33/oc-cg-p10` (you can also download the code as a [ZIP archive](https://github.com/CeeG33/oc-cg-p10/archive/refs/heads/main.zip)
2. Navigate to the root directory of the oc-cg-p10 repository using a terminal with the command `$ cd oc-cg-p10`
3. Create a virtual environment for the project with `$ python -m venv env` on Windows or `$ python3 -m venv env` on MacOS or Linux.
4. Activate the virtual environment with `$ env\Scripts\activate` on Windows or `$ source env/bin/activate` on MacOS or Linux.
5. Install project dependencies using the command `$ pip install -r requirements.txt`
6. Start the server with `$ python manage.py runserver`

When the server is running (after step 6 of the procedure), the SoftDesk Support API can be queried from the entry points starting with the base URL [http://127.0.0.1:8000/api/](http://127.0.0.1:8000/api/). 

Steps 1 to 3 are only required for the initial installation. For subsequent launches of the API server, simply execute steps 4 to 6 from the project's root directory.

## Pre-existing Accounts

Here is a list of users created for illustration purposes:

```
Login : admin - Password : admin << Administrator account
Login : Maxime - Password : maxime
Login : Pierre - Password : pierre
Login : Julie - Password : julie
Login : Célia - Password : celia
```


## Entry Points Usage and Documentation

The API provides the following entry points:

| Endpoints  | Allowed Requests | Prerequisites | Uses |
| :---:        | :---:                | :---         | :---           |
| api/token/ | POST      | Sign in with an existing account | Get a token to access the API |
| api/<br>user/  | GET, POST | Be authenticated                         | View the list of users or create a new user |
| api/<br>user/<br><user_pk>/ | GET, PUT, PATCH, DELETE | Read: Be authenticated; Modification: Only the user in question can modify or delete their data | View or modify/delete user details. Note: Only pages of users who have agreed to share their data can be viewed |
| api/<br>project/ | GET, POST | Be authenticated | View the list of projects or create a new project. Note: Only projects on which the user is a contributor will be displayed |
| api/<br>project/<br><project_pk>/ | GET, PUT, PATCH, DELETE | Read: Be authenticated and a project contributor; Modification: Be the author of the project | View or modify/delete project details |
| api/<br>project/<br><project_pk>/<br>issue/ | GET, POST | Be authenticated and a project contributor | View the list of issues or create a new issue on a given project. Note: Only issues from the selected project will be displayed |
| api/<br>project/<br><project_pk>/<br>issue/<br><issue_pk> | GET, PUT, PATCH, DELETE | Read: Be authenticated and a project contributor; Modification: Be the author of the issue | View or modify/delete issue details |
| api/<br>project/<br><project_pk>/<br>issue/<br><issue_pk>/<br>comment/ | GET, POST | Be authenticated and a project contributor | View the list of comments or create a new comment on a given issue. Note: Only comments from the selected issue will be displayed |
| api/<br>project/<br><project_pk>/<br>issue/<br><issue_pk>/<br>comment/<br><comment_pk>/ | GET, PUT, PATCH, DELETE | Read: Be authenticated and a project contributor; Modification: Be the author of the comment | View or modify/delete comment details |

The endpoints Postman documentation can also be seen [here](https://documenter.getpostman.com/view/29348288/2s9YBxZwPn#intro).

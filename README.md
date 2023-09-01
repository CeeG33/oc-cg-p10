# SoftDesk Support API: API de gestion de problèmes techniques

SoftDesk Support API est une application web à éxecuter localement. Il s'agit d'un outil permettant permettant de remonter et suivre des problèmes techniques. Cette application est implémentée sous la forme d'une API REST. Elle permet la lecture et la création d'utilisateurs et de projets contenants des tickets et des commentaires. Ces actions sont possibles à partir d'URLs interrogeables à l'aide de Postman. Les points d'entrées fournis par cette API et les requêtes GET réalisables sont détaillés dans les sections suivantes.

## Installation

Cette API exécutable localement peut être installée en suivant les étapes décrites ci-dessous. L'usage de Poetry est recommandé, mais des instuctions utilisant venv et pip sont également fournies plus bas. Si pipenv n'est pas encore installé sur votre ordinateur, vous trouverez des instuctions d'installation détaillées [sur cette page](https://python-poetry.org/docs/basic-usage/).

### Installation et exécution de l'application avec Poetry

1. Clonez ce dépôt de code à l'aide de la commande `$ git clone clone https://github.com/CeeG33/oc-cg-p10` (vous pouvez également télécharger le code [en tant qu'archive zip](https://github.com/CeeG33/oc-cg-p10/archive/refs/heads/main.zip)
2. Rendez vous depuis un terminal à la racine du répertoire oc-cg-p10 avec la commande `$ cd oc-cg-p10`
3. Installez les dépendances du projet à l'aide de la commande `poetry install` 
4. Démarrez le serveur avec `poetry run python manage.py runserver`

Lorsque le serveur fonctionne (après l'étape 4 de la procédure), l'API SoftDesk Support peut être interrogée à partir des points d'entrée commençant par l'url de base [http://127.0.0.1:8000/api/](http://127.0.0.1:8000/api/). 

Les étapes 1 à 3 ne sont requises que pour l'installation initiale. Pour les lancements ultérieurs du serveur de l'API, il suffit d'exécuter l'étape 4 à partir du répertoire racine du projet.

### Installation et exécution de l'application sans Poetry (avec venv et pip)

1. Clonez ce dépôt de code à l'aide de la commande `$ git clone clone https://github.com/CeeG33/oc-cg-p10` (vous pouvez également télécharger le code [en tant qu'archive zip](https://github.com/CeeG33/oc-cg-p10/archive/refs/heads/main.zip)
2. Rendez vous depuis un terminal à la racine du répertoire oc-cg-p10 avec la commande `$ cd oc-cg-p10`
3. Créez un environnement virtuel pour le projet avec `$ python -m venv env` sous Windows ou `$ python3 -m venv env` sous MacOS ou Linux.
4. Activez l'environnement virtuel avec `$ env\Scripts\activate` sous Windows ou `$ source env/bin/activate` sous MacOS ou Linux.
5. Installez les dépendances du projet avec la commande `$ pip install -r requirements.txt`
6. Démarrez le serveur avec `python manage.py runserver`

Lorsque le serveur fonctionne (après l'étape 4 de la procédure), l'API SoftDesk Support peut être interrogée à partir des points d'entrée commençant par l'url de base [http://127.0.0.1:8000/api/](http://127.0.0.1:8000/api/). 

Les étapes 1 à 3 ne sont requises que pour l'installation initiale. Pour les lancements ultérieurs du serveur de l'API, il suffit d'exécuter les étapes 4 à 6 à partir du répertoire racine du projet.

## Utilisation et documentation des points d'entrée

L'API fournit les points d'entrées suivants: 


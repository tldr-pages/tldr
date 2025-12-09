# pipenv

> Workflow de développement simple et unifié pour Python.
> Gère les paquets et l'environnement virtuel d'un projet.
> Plus d'informations : <https://pypi.org/project/pipenv>.

- Crée un nouveau projet :

`pipenv`

- Crée un nouveau projet à l'aide de Python 3 :

`pipenv --three`

- Installe un paquet :

`pipenv install {{paquet}}`

- Installe toutes les dépendances d'un projet :

`pipenv install`

- Installe toutes les dépendances d'un projet (y compris les paquets de développement) :

`pipenv install --dev`

- Désinstalle un paquet :

`pipenv uninstall {{paquet}}`

- Démarre une session de commandes dans l'environnement virtuel :

`pipenv shell`

- Génère un `requirements.txt` (une liste de dépendances) pour un projet :

`pipenv lock --requirements`

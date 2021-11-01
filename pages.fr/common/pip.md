# pip

> Gestionnaire des paquets pour Python.
> Certaines commandes comme `pip install` ont leur propre documentation.
> Plus d'informations : <https://pip.pypa.io>.

- Installe un paquet :

`pip install {{paquet}}`

- Installe une version particulière d'un paquet :

`pip install {{paquet}}=={{version}}`

- Installe un paquet dans le répertoire utilisateur au lieu de l'emplacement par défaut système :

`pip install --user {{paquet}}`

- Met à jour un paquet :

`pip install --upgrade {{paquet}}`

- Désinstalle un paquet :

`pip uninstall {{paquet}}`

- Sauvegarde une liste des paquets installés :

`pip freeze > {{requirements.txt}}`

- Installe des paquets à partir d'un fichier :

`pip install --requirement {{requirements.txt}}`

- Affiche les informations d'un paquet installé :

`pip show {{paquet}}`

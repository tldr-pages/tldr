# pip

> Gestionnaire des paquets pour Python.
> Plus d'informations : <https://pip.pypa.io>.

- Installe un paquet:

`pip install {{paquet}}`

- Installe une version particulière d'un paquet:

`pip install {{paquet}}=={{version}}`

- Installer un package dans le répertoire de l'utilisateur au lieu de l'emplacement par défaut à l'échelle du système:

`pip install --user {{paquet}}`

- Met à jour un paquet:

`pip install --upgrade {{paquet}}`

- Désinstalle un paquet:

`pip uninstall {{paquet}}`

- Sauvegarde une liste des paquets installés:

`pip freeze > {{requirements.txt}}`

- Installe des paquets à partir d'un fichier:

`pip install --requirement {{requirements.txt}}`

- Affiche les informations d'un paquet installé:

`pip show {{paquet}}`

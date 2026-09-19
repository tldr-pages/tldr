# pip

> Gestionnaire des paquets pour Python.
> Certaines sous-commandes comme `install` ont leur propre documentation.
> Plus d'informations : <https://pip.pypa.io/en/stable/cli/pip/>.

- Installe un paquet (voir `pip install` pour plus d'exemples d'installation) :

`pip install {{paquet}}`

- Installe un paquet dans le répertoire de l'utilisateur au lieu de l'emplacement par défaut système :

`pip install --user {{paquet}}`

- Met à niveau un paquet :

`pip install {{[-U|--upgrade]}} {{paquet}}`

- Désinstalle un paquet :

`pip uninstall {{paquet}}`

- Sauvegarde les paquets installés à un fichier :

`pip freeze > {{requirements.txt}}`

- Liste les paquets installés :

`pip list`
- Affiche les informations d'un paquet installé :

`pip show {{paquet}}`
- Installe des paquets à partir d'un fichier :

`pip install {{[-r|--requirement]}} {{requirements.txt}}`

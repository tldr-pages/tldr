# code

> Éditeur de code multiplateforme et extensible.
> Plus d'informations : <https://github.com/microsoft/vscode>.

- Démarre Visual Studio Code :

`code`

- Ouvre des fichiers/répertoires spécifiques :

`code {{chemin/vers/fichier_ou_répertoire1 chemin/vers/fichier_ou_répertoire2 ...}}`

- Compare deux fichiers spécifiques :

`code --diff {{chemin/vers/fichier1}} {{chemin/vers/fichier2}}`

- Ouvre des fichiers/répertoires spécifiques dans une nouvelle fenêtre :

`code --new-window {{chemin/vers/fichier_ou_répertoire1 chemin/vers/fichier_ou_répertoire2 ...}}`

- Installe/désinstalle une extension spécifique :

`code --{{install|uninstall}}-extension {{éditeur.extension}}`

- Affiche les extensions installées :

`code --list-extensions`

- Affiche les extensions installées avec leurs versions :

`code --list-extensions --show-versions`

- Démarre l'éditeur en tant que super utilisateur (root) tout en stockant les données utilisateur dans un répertoire spécifique :

`sudo code --user-data-dir {{chemin/vers/répertoire}}`

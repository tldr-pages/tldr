# zip

> Empaquette et compresse (archive) les fichiers en un fichier zip.
> Plus d'informations : <https://manned.org/zip>.

- Empaquette et compresse [r]écursivement un répertoire et son contenu :

`zip {{[-r|--recurse-paths]}} {{archive.zip}} {{chemin/du/répertoire}}`

- E[x]clure des fichiers de l'archive :

`zip {{[-r|--recurse-paths]}} {{archive.zip}} {{chemin/vers/le/répertoire}} {{[-x|--exclude]}} {{chemin/des/fichiers/exclus}}`

- Archive un répertoire et son contenu avec le plus haut niveau [9] de compression :

`zip {{[-r|--recurse-paths]}} -{{9}} {{archive.zip}} {{chemin/du/répertoire}}`

- Empaquette et compresse plusieurs répertoires et fichiers :

`zip {{[-r|--recurse-paths]}} {{archive.zip}} {{chemin/du/répertoire1 chemin/du/répertoire2 chemin/du/fichier}}`

- Crée une archive chiffrée (l'utilisateur sera sollicité pour saisir le mot de passe) :

`zip {{[-re|--recurse-paths --encrypt]}} {{archive.zip}} {{chemin/du/répertoire}}`

- Ajoute des fichiers à une archive existante :

`zip {{archive.zip}} {{chemin/du/fichier}}`

- Supprime des fichiers d'une archive existante :

`zip {{[-d|--delete]}} {{archive.zip}} "{{foo/*.tmp}}"`

- Archive un répertoire et son contenu en plusieurs fichiers zip [s]cindés (ex : des fichiers de 3 Go) :

`zip {{[-rs|--recurse-paths --split-size]}} {{3g}} {{archive.zip}} {{chemin/du/répertoire}}`

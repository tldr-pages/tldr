# zip

> Empaquette et compresse (archive) les fichiers en un fichier zip.
> Plus d'informations : <https://manned.org/zip>.

- Empaquette et compresse [r]écursivement un répertoire et son contenu :

`zip -r {{archive.zip}} {{chemin/du/répertoire}}`

- E[x]clure des fichiers de l'archive :

`zip -r {{archive.zip}} {{chemin/vers/le/répertoire}} -x {{chemin/des/fichiers/exclus}}`

- Archive un répertoire et son contenu avec le plus haut niveau [9] de compression :

`zip -r -{{9}} {{archive.zip}} {{chemin/du/répertoire}}`

- Empaquette et compresse plusieurs répertoires et fichiers :

`zip -r {{archive.zip}} {{chemin/du/répertoire1 chemin/du/répertoire2 chemin/du/fichier}}`

- Crée une archive chiffrée (l'utilisateur sera sollicité pour saisir le mot de passe) :

`zip -e -r {{archive.zip}} {{chemin/du/répertoire}}`

- Ajoute des fichiers à une archive existante :

`zip {{archive.zip}} {{chemin/du/fichier}}`

- Supprime des fichiers d'une archive existante :

`zip -d {{archive.zip}} "{{foo/*.tmp}}"`

- Archive un répertoire et son contenu en plusieurs fichiers zip [s]cindés (ex : des fichiers de 3 Go) :

`zip -r -s {{3g}} {{archive.zip}} {{chemin/du/répertoire}}`

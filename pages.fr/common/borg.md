# borg

> Outil de sauvegarde avec déduplication.
> Crée des sauvegarde distante ou locale qui peuvent être montée comme un système de fichier.
> Pour plus d'information: <https://borgbackup.readthedocs.io/en/stable/usage/general.html>.

- Initialise un dépôt local:

`borg init {{/path/to/repo_directory}}`

- Sauvegarde un répertoire dans le dépôt en créant une archive appelée "Monday":

`borg create --progress {{/path/to/repo_directory}}::{{Monday}} {{/path/to/source_directory}}`

- Liste toutes les archives d'un dépôt:

`borg list {{/path/to/repo_directory}}`

- Extrait un répertoire donné de l'archive nommée "Monday" à partir d'un dépôt distant tout en excluant tous les fichiers *.ext:

`borg extract {{user}}@{{host}}:{{/path/to/repo_directory}}::{{Monday}} {{path/to/target_directory}} --exclude '{{*.ext}}'`

- Néttoie un dépôt en effaçant toutes les archives agées de plus de 7 jours tout en affichant les changements:

`borg prune --keep-within {{7d}} --list {{/path/to/repo_directory}}`

- Monte un dépôt comme un système de fichier FUSE:

`borg mount {{/path/to/repo_directory}}::{{Monday}} {{/path/to/mountpoint}}`

- Affiche l'aide sur la création d'archive:

`borg create --help`

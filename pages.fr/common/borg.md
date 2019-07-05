# borg

> Outil de sauvegarde avec déduplication.
> Crée des sauvegardes distantes ou locales qui peuvent être montées comme un système de fichiers.
> Pour plus d'informations: <https://borgbackup.readthedocs.io/en/stable/usage/general.html>.

- Initialise un dépôt local:

`borg init {{/path/to/repo_directory}}`

- Sauvegarde un répertoire dans le dépôt en créant une archive appelée "Lundi":

`borg create --progress {{/path/to/repo_directory}}::{{Lundi}} {{/path/to/source_directory}}`

- Liste toutes les archives d'un dépôt:

`borg list {{/path/to/repo_directory}}`

- Extrait un répertoire donné de l'archive nommée "Lundi" à partir d'un dépôt distant tout en excluant tous les fichiers *.ext:

`borg extract {{utilisateur}}@{{host}}:{{/path/to/repo_directory}}::{{Lundi}} {{path/to/target_directory}} --exclude '{{*.ext}}'`

- Nettoie un dépôt en effaçant toutes les archives âgées de plus de 7 jours tout en affichant les changements:

`borg prune --keep-within {{7d}} --list {{/path/to/repo_directory}}`

- Monte un dépôt comme un système de fichiers FUSE:

`borg mount {{/path/to/repo_directory}}::{{Lundi}} {{/path/to/mountpoint}}`

- Affiche l'aide sur la création d'archives:

`borg create --help`

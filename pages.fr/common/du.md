# du

> Utilisation de disque : estime et résume l'utilisation de l'espace occupé par les fichiers et les répertoires.
> Plus d'informations : <https://www.gnu.org/software/coreutils/manual/html_node/du-invocation.html>.

- Liste les tailles d'un répertoire et de ses sous-répertoires, dans l'unité donnée (o/Kio/Mio) :

`du -{{b|k|m}} {{chemin/vers/répertoire}}`

- Liste les tailles d'un répertoire et de ses sous-répertoires, sous une forme lisible par l'homme (c'est-à-dire en sélectionnant automatiquement l'unité appropriée pour chaque taille) :

`du {{[-h|--human-readable]}} {{chemin/vers/répertoire}}`

- Affiche la taille d'un répertoire unique, en unités lisibles par l'homme :

`du {{[-sh|--summarize --human-readable]}} {{chemin/vers/répertoire}}`

- Liste les tailles, en unités lisibles par l'homme, d'un répertoire et de tous les fichiers et répertoires qu'il contient :

`du {{[-ah|--all --human-readable]}} {{chemin/vers/répertoire}}`

- Liste les tailles, en unités lisibles par l'homme, d'un répertoire et de ses sous-répertoires, jusqu'à N niveaux de profondeur :

`du {{[-h|--human-readable]}} {{[-d|--max-depth]}} N {{chemin/vers/répertoire}}`

- Liste la taille, en unités lisible par l'homme, de tous les fichiers `.jpg` dans les sous-répertoires du répertoire courant, et affiche un total cumulatif à la fin :

`du {{[-ch|--total --human-readable]}} {{*/*.jpg}}`

- Liste tous les fichiers et répertoires (y compris les fichiers cachés) dépassant un certain seuil (utile pour déterminer ce qui occupe réellement l'espace) :

`du {{[-ah|--all --human-readable]}} {{[-t|--threshold]}} {{1G|1024M|1048576K}} .[^.]* *`

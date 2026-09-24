# dex

> DesktopEntry Execution est un programme servant à générer et à exécuter des fichiers DesktopEntry de type Application.
> Plus d'informations : <https://github.com/jceb/dex#dex>.

- Exécute tous les programmes dans les répertoires de démarrage automatique :

`dex {{[-a|--autostart]}}`

- Exécute tous les programmes dans les répertoires spécifiés :

`dex {{[-a|--autostart]}} {{[-s|--search-paths]}} {{chemin/vers/répertoire1}}:{{chemin/vers/répertoire2}}:{{chermin/vers/répertoire3}}:`

- Prévisualise les programmes qui seraient exécutés lors d'un démarrage automatique spécifique à GNOME :

`dex {{[-a|--autostart]}} {{[-e|--environment]}} {{GNOME}}`

- Prévisualise les programmes qui seraient exécutés lors d'un démarrage automatique standard :

`dex {{[-a|--autostart]}} {{[-d|--dry-run]}}`

- Prévisualise la valeur de la propriété `Name` de DesktopEntry :

`dex {{[-p|--property]}} {{Name}} {{chemin/vers/fichier.desktop}}`

- Crée une DesktopEntry pour un programme dans le répertoire actuel :

`dex {{[-c|--create]}} {{chemin/vers/fichier.destkop}}`

- Exécute un programme (avec `Terminal=true` dans le fichier Desktop) dans le terminal donné :

`dex --term {{terminal}} {{chemin/vers/fichier.desktop}}`

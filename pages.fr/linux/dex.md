# dex

> DesktopEntry Execution est un programme servant à générer et à exécuter des fichiers DesktopEntry de type Application.
> Plus d'informations : <https://github.com/jceb/dex>.

- Exécute tous les programmes dans les dossiers de démarrage automatique :

`dex --autostart`

- Exécute tous les programmes dans les dossiers spécifiés :

`dex --autostart --search-paths {{chemin/vers/dossier1}}:{{chemin/vers/dossier2}}:{{chermin/vers/dossier3}}:`

- Prévisualise les programmes qui seraient exécutés lors d'un démarrage automatique spécifique à GNOME :

`dex --autostart --environment {{GNOME}}`

- Prévisualise les programmes qui seraient exécutés lors d'un démarrage automatique standard :

`dex --autostart --dry-run`

- Prévisualise la valeur de la propriété `Name` de DesktopEntry :

`dex -- property {{Name}} {{chemin/vers/fichier.desktop}}`

- Crée une DesktopEntry pour un programme dans le dossier courant :

`dex --create {{chemin/vers/fichier.destkop}}`

- Exécute un programme (avec `Terminal=true` dans le fichier Desktop) dans le terminal donné :

`dex --term {{terminal}} {{chemin/vers/fichier.desktop}}`

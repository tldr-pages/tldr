# winget

> Gestionnaire de paquets Windows.
> Plus d'informations : <https://learn.microsoft.com/windows/package-manager/winget>.

- Installer un paquet :

`winget {{[add|install]}} {{paquet}}`

- Supprimer un paquet (Remarque : `remove` peut aussi être utilisé à la place de `uninstall`) :

`winget {{[rm|uninstall]}} {{paquet}}`

- Afficher des informations sur un paquet :

`winget show {{paquet}}`

- Rechercher un paquet :

`winget search {{paquet}}`

- Mettre à jour tous les paquets vers les dernières versions :

`winget upgrade {{[-r|--all]}}`

- Lister tous les paquets installés qui peuvent être gérés avec `winget` :

`winget {{[ls|list]}} {{[-s|--source]}} winget`

- Importer des paquets depuis un fichier, ou exporter les paquets installés vers un fichier :

`winget {{import|export}} {{--import-file|--output}} {{chemin/vers/fichier}}`

- Valider des manifestes avant de soumettre une PR au dépôt winget-pkgs :

`winget validate {{chemin/vers/manifeste}}`

# winget

> Gestionnaire de paquets Windows.
> Plus d'informations : <https://learn.microsoft.com/windows/package-manager/winget>.

- Installe un paquet :

`winget {{[add|install]}} {{paquet}}`

- Supprime un paquet (remarque : `remove` peut aussi être utilisé à la place de `uninstall`) :

`winget {{[rm|uninstall]}} {{paquet}}`

- Affiche des informations sur un paquet :

`winget show {{paquet}}`

- Recherche un paquet :

`winget search {{paquet}}`

- Met à jour tous les paquets vers les dernières versions :

`winget upgrade {{[-r|--all]}}`

- Liste tous les paquets installés qui peuvent être gérés avec `winget` :

`winget {{[ls|list]}} {{[-s|--source]}} winget`

- Importe des paquets depuis un fichier, ou exporte les paquets installés vers un fichier :

`winget {{import|export}} {{--import-file|--output}} {{chemin/vers/fichier}}`

- Valide des manifestes avant de soumettre une PR au dépôt winget-pkgs :

`winget validate {{chemin/vers/manifeste}}`

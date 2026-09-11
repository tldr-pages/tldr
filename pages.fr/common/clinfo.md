# clinfo

> Afficher les plateformes et les périphériques OpenCL.
> Plus d'informations : <https://manned.org/man/clinfo>.

- Affiche les informations sur toutes les plateformes et tous les périphériques OpenCL :

`clinfo`

- Énumère les plateformes et les appareils par nom :

`clinfo {{[-l|--list]}}`

- Affiche les informations relatives à un appareil spécifique :

`clinfo {{[-d|--device]}} {{index_platforme}}:{{index_appareil}}`

- Affiche une sortie adaptée aux machines :

`clinfo --raw`

- Inclut les appareils hors ligne :

`clinfo --offline`

- Tente de récupérer toutes les propriétés, y compris celles qui ne sont pas officielles :

`clinfo {{[-a|--all-props]}}`

- Affiche uniquement les propriétés correspondant au nom de propriété indiqué :

`clinfo --prop {{nom_propriété}}`

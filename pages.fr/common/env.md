# env

> Affiche l'environnement ou exécute un programme dans un environnement modifié.
> Plus d'informations : <https://www.gnu.org/software/coreutils/env>.

- Affiche l'environnement :

`env`

- Exécute le programme donné. Souvent utilisé dans les scripts après le shebang (`#!`) pour consulter le chemin vers le programme :

`env {{programme}}`

- Exécute le programme donné, avec un environnement vide :

`env -i {{programme}}`

- Supprime une variable d'environnement et execute le programme donné :

`env -u {{variable}} {{programme}}`

- Définit ou modifie une variable d'environnement et execute le programme donné :

`env {{variable}}={{valeur}} {{programme}}`

- Définit ou modifie plusieurs variables d'environnement et execute le programme donné :

`env {{variable1}}={{valeur}} {{variable2}}={{valeur}} {{variable3}}={{valeur}} {{programme}}`

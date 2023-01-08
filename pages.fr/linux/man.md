# man

> Interface de consultation des pages du manuel de référence.
> Plus d'informations : <https://manned.org/man>.

- Affiche la page de manuel d'une commande :

`man {{commande}}`

- Affiche la page de manuel de la section 7 d'une commande :

`man {{7}} {{commande}}`

- Liste toutes les sections dans lesquelles se trouve une commande :

`man --whatis {{commande}}`

- Affiche tous les chemins où se trouvent les pages de manuel :

`man --path`

- Affiche l'emplacement d'une page de manuel plutôt que la page elle-même :

`man --where {{commande}}`

- Affiche la page de manuel dans une langue particulière :

`man --locale={{fr_FR}} {{commande}}`

- Cherche toutes les pages de manuel contenant la chaîne de caractères spécifée :

`man --apropos "{{chaîne_de_caractères}}"`

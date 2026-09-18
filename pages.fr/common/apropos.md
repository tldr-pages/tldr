# apropos

> Recherche dans les pages de manuel, par exemple pour trouver une nouvelle commande.
> Voir aussi : `man`.
> Plus d'informations : <https://manned.org/apropos>.

- Recherche par mot clé :

`apropos {{regex}}`

- Recherche sans limiter la sortie à la largeur du terminal :

`apropos {{[-l|--long]}} {{regex}}`

- Recherche les pages qui contiennent toutes les `regex` (fonction ET) :

`apropos {{regex_1}} {{[-a|--and]}} {{regex_2}} {{[-a|--and]}} {{regex_3}}`

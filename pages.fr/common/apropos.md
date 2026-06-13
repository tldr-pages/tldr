# apropos

> Recherche dans les pages de manuel, par exemple pour trouver une nouvelle commande.
> Voir aussi : `man`.
> Plus d'informations : <https://manned.org/apropos>.

- Recherche par mot clé :

`apropos {{expression_reguliere}}`

- Recherche sans limiter la sortie à la largeur du terminal :

`apropos {{[-l|--long]}} {{expression_reguliere}}`

- Recherche les pages qui contiennent toutes les expressions données (fonction ET) :

`apropos {{expression_reguliere_1}} {{[-a|--and]}} {{expression_reguliere_2}} {{[-a|--and]}} {{expression_reguliere_3}}`

# apropos

> Recherche dans les pages de manuel, par exemple pour trouver une nouvelle commande.

- Recherche par mot clé :

`apropos {{expression_reguliere}}`

- Recherche sans limiter la sortie à la largeur du terminal :

`apropos -l {{expression_reguliere}}`

- Recherche les pages qui contiennent toutes les expressions données (fonction ET) :

`apropos {{expression_reguliere_1}} -a {{expression_reguliere_2}} -a {{expression_reguliere_3}}`

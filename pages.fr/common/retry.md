# retry

> Répète une commande jusqu’à ce qu’elle réussisse ou qu’un critère soit rempli.
> Plus d'informations : <https://manned.org/retry>.

- Réessaie une commande jusqu’à ce qu’elle réussisse :

`retry {{commande}}`

- Réessaie une commande toutes les n secondes jusqu’à ce qu’elle réussisse :

`retry {{[-d|--delay]}} {{n}} {{commande}}`

- Abandonne après n tentatives :

`retry {{[-t|--times]}} {{n}} {{commande}}`

# atq

> Affiche les travaux programmés par la commande `at` ou `batch`.
> Plus d'informations : <https://manned.org/atq>.

- Affiche les travaux programmés de l'utilisateur courant :

`atq`

- Affiche les travaux de la file nommé 'a' (les files ont des noms avec une seule lettre) :

`atq -q {{a}}`

- Affiche les travaux de tous les utilisateurs (lancé en tant que super-utilisateur) :

`sudo atq`

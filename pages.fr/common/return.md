# return

> Quitte une fonction.
> Peut quitter un script s’il est exécuté avec `source`.
> Voir aussi : `exit`.
> Plus d'informations : <https://www.gnu.org/software/bash/manual/bash.html#index-return>.

- Quitte prématurément une fonction :

`{{nom_fonc}}() { {{echo "Ceci est atteint"}}; return; {{echo "Ceci n’est pas atteint"}}; }`

- Définit la valeur de retour de la fonction :

`{{nom_fonc}}() { return {{valeur_retour}}; }`

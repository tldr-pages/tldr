# git bisect

> Utiliser une recherche binaire pour trouver le commit qui a introduit un bug.
> Git saute automatiquement d'avant en arrière dans le graphe de commit pour isoler le commit défectueux.
> Plus d'informations : <https://git-scm.com/docs/git-bisect>.

- Démarrez une dissection sur une plage de commit délimitée par un bug connu et un commit propre connu (généralement plus ancien) :

`git bisect start {{bad_commit}} {{good_commit}}`

- Pour chaque `git bisect` sélectionné, le marquer comme "mauvais" (`bad`) ou "bon" (`good`) après l'avoir testé pour le problème :

`git bisect {{good|bad}}`

- Après que `git bisect` pointe vers le mauvais commit, terminer la dissection et retourner à la branche précédente :

`git bisect reset`

- Sauter un commit lors de la dissection (e.g. celui qui échoue les tests pour une autre raison) :

`git bisect skip`

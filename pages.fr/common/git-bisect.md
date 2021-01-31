# git bisect

> Utiliser une recherche binaire pour trouver le commit qui a introduit un bug.
> Git saute automatiquement d'avant en arrière dans le graphe de commit pour isoler le commit défectueux.
> Plus d'informations : <https://git-scm.com/docs/git-bisect>.

- Démarrez une dissection sur une plage de commit délimitée par un bug connu et un commit propre connu (généralement plus ancien) :

`git bisect start {{bad_commit}} {{good_commit}}`

- Pour chaque `git bisect` selectionné, le marquer comme "bad" ou "good" apres l'avoir testé pour le probléme :

`git bisect {{good|bad}}`

- Apres que `git bisect` pointe vers le mauvais commit, terminer la dissection et retourner a la branche précedante :

`git bisect reset`

- Sauter un commit lorrs de la dissection (e.g. celui qui echoue les tests pour une autre raison) :

`git bisect skip`

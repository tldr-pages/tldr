# git rebase

> Rejoue les commits d'une branche par dessus une autre.
> Communément utilisé pour dupliquer les commits d'une branche dans une autre, en créant de nouveaux commits dans la branche de destination.
> Plus d'informations : <https://git-scm.com/docs/git-rebase>.

- Rejouer les commits de la branche courante sur la branche master :

`git rebase {{master}}`

- Rejouer les comits interactivement, ce qui permet aux commits d'être re-arrangés, exclus, combinés ou modifiés :

`git rebase -i {{branche_de_base_ou_commit}}`

- Continuer le re-jeu des commits après la résolution d'un conflit :

`git rebase --continue`

- Continuer le re-jeu des commits en sautant la résolution d'un conflit :

`git rebase --skip`

- Annule l'opération (ex : en cas de conflit) :

`git rebase --abort`

- Déplacez une partie de la branche actuelle sur une nouvelle base, fournissant l'ancienne base à partir de laquelle commencer :

`git rebase --onto {{new_base}} {{old_base}}`

- Rejoue les 5 derniers commits, ce qui permet aux commits d'être re-arrangés, exclus, combinés ou modifiés :

`git rebase -i {{HEAD~5}}`

- Résoudre automatiquement les conflits en précisant la version à conserver (`theirs` signifie la version des fichiers à privilégier) :

`git rebase -X theirs {{master}}`

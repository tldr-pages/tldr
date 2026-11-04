# git rebase

> Rejoue les validations d'une branche par dessus une autre.
> Communément utilisé pour dupliquer les validations d'une branche dans une autre, en créant de nouvelles validations dans la branche de destination.
> Plus d'informations : <https://git-scm.com/docs/git-rebase>.

- Rejoue les validations de la branche actuelle sur la branche master :

`git rebase {{master}}`

- Rejoue les validations interactivement, ce qui permet aux validations d'être re-arrangées, exclues, combinées ou modifiées :

`git rebase {{[-i|--interactive]}} {{branche_base_ou_validation}}`

- Continue le re-jeu des validations après la résolution d'un conflit :

`git rebase --continue`

- Continue le re-jeu des validations en sautant la résolution d'un conflit :

`git rebase --skip`

- Annule l'opération (ex : en cas de conflit) :

`git rebase --abort`

- Déplace une partie de la branche actuelle sur une nouvelle base, fournissant l'ancienne base à partir de laquelle commencer :

`git rebase --onto {{nouvelle_base}} {{ancienne_base}}`

- Rejoue les 5 dernières validations, ce qui permet aux validations d'être re-arrangées, exclues, combinées ou modifiées :

`git rebase {{[-i|--interactive]}} HEAD~5`

- Résout automatiquement les conflits en précisant la version à conserver (`theirs` signifie la version des fichiers à privilégier) :

`git rebase {{[-X|--strategy-option]}} theirs {{master}}`

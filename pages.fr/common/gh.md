# gh

> Travailler harmonieusement avec GitHub depuis la ligne de commande. Certaines sous-commandes telles que `gh config` ont leur propre documentation d'usage.
> Plus d'informations : <https://cli.github.com/>.

- Cloner un dépôt GitHub localement :

`gh repo clone {{utilisateur}}/{{dépôt}}`

- Créer une nouvelle issue :

`gh issue create`

- Voir et filtrer les issues ouvertes du dépôt courant :

`gh issue list`

- Voir une issue dans le navigateur Web par défaut :

`gh issue view --web {{numéro_de_l'issue}}`

- Créer une pull request :

`gh pr create`

- Voiir une pull request dans le navigateur Web par défaut :

`gh pr view --web {{numéro_de_la_PR}}`

- Observer une pull request spécifique localement :

`gh pr checkout {{numéro_de_la_PR}}`

- Regarder le statut des pull requests d'un dépôt :

`gh pr status`

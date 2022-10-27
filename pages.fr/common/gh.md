# gh

> Travailler harmonieusement avec GitHub depuis la ligne de commande.
> Certaines commandes comme `gh config` ont leur propre documentation.
> Plus d'informations : <https://cli.github.com/>.

- Clone un dépôt GitHub localement :

`gh repo clone {{utilisateur}}/{{dépôt}}`

- Crée une nouvelle issue :

`gh issue create`

- Affiche et filtre les issues ouvertes du dépôt courant :

`gh issue list`

- Affiche une issue dans le navigateur Web par défaut :

`gh issue view --web {{numéro_de_l'issue}}`

- Crée une pull request :

`gh pr create`

- Affiche une pull request dans le navigateur Web par défaut :

`gh pr view --web {{numéro_de_la_PR}}`

- Observe une pull request spécifique localement :

`gh pr checkout {{numéro_de_la_PR}}`

- Affiche le statut des pull requests du dépôt courant:

`gh pr status`

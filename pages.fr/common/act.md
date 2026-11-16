# act

> Exécute des GitHub Actions en local avec Docker.
> Plus d'informations : <https://manned.org/act>.

- [l]iste les jobs disponibles :

`act {{[-l|--list]}}`

- Exécute l'événement par défault :

`act`

- Exécute un événement spécifique :

`act {{type_d_événement}}`

- Exécute un [j]ob spécifique :

`act {{[-j|--job]}} {{id_job}}`

- Ne lance pas les actions maintenant (e.g un essai) :

`act {{[-n|--dryrun]}}`

- Affiche le journal en mode verbeux :

`act {{[-v|--verbose]}}`

- Exécute un [W]orkflow en particulier, avec l'événement push :

`act push {{[-W|--workflows]}} {{path/to/workflow}}`

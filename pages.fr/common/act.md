# act

> Execute des GitHub Actions en local avec Docker.
> Plus d'informations : <https://manned.org/act>.

- [l]iste les jobs disponibles :

`act {{[-l|--list]}}`

- Execute l'événement par défault :

`act`

- Execute un événement spécifique :

`act {{type_d_événement}}`

- Execute un [j]ob spécifique :

`act {{[-j|--job]}} {{id_job}}`

- Ne pas lancer les actions maintenant (e.g un essai) :

`act {{[-n|--dryrun]}}`

- Affiche le journal en mode verbeux :

`act {{[-v|--verbose]}}`

- Execute un [W]orkflow en particulier, avec l'événement push :

`act push {{[-W|--workflows]}} {{path/to/workflow}}`

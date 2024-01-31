# act

> Execute des GitHub Actions en local avec Docker.
> Plus d'informations : <https://github.com/nektos/act>.

- [l]iste les jobs disponibles :

`act -l`

- Execute l'événement par défault :

`act`

- Execute un événement spécifique :

`act {{type_d_événement}}`

- Execute un [j]ob spécifique :

`act -j {{id_job}}`

- Ne pas lancer les actions maintenant (e.g un essai) :

`act -n`

- Affiche le journal en mode verbeux :

`act -v`

- Execute un [W]orkflow en particulier, avec l'événement push :

`act push -W {{path/to/workflow}}`

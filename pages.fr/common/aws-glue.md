# aws glue

> CLI pour AWS Glue.
> Définie un endpoint publique pour le service AWS Glue.
> Plus d'informations : <https://docs.aws.amazon.com/cli/latest/reference/glue/>.

- Liste les tâches :

`aws glue list-jobs`

- Démarre une tâche :

`aws glue start-job-run --job-name {{nom_de_la_tâche}}`

- Démarre un flux de travail :

`aws glue start-workflow-run --name {{nom_flux_de_travail}}`

- Liste les déclencheurs :

`aws glue list-triggers`

- Démarre un déclencheur :

`aws glue start-trigger --name {{nom_du_déclencheur}}`

- Créé un endpoint de développement :

`aws glue create-dev-endpoint --endpoint-name {{nom}} --role-arn {{rôle_arn_utilisé_par_l_endpoint}}`

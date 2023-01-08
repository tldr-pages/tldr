# aws lambda

> CLI pour AWS lambda.
> Plus d'informations : <https://docs.aws.amazon.com/cli/latest/reference/lambda/>.

- Lance une fonction :

`aws lambda invoke --function-name {{nom}} {{chemin/vers/la/réponse}}.json`

- Lance une fonction avec pour donnée d'entrée, un document JSON :

`aws lambda invoke --function-name {{nom}} --payload {{json}} {{chemin/vers/la/réponse}}.json`

- Liste les fonctions :

`aws lambda list-functions`

- Affiche la configuration d'une fonction :

`aws lambda get-function-configuration --function-name {{nom}}`

- Affiche les alias d'une fonction :

`aws lambda list-aliases --function-name {{nom}}`

- Affiche la configuration de concurrence pour une fonction :

`aws lambda get-function-concurrency --function-name {{nom}}`

- Affiche quel service AWS peut appeler une fonction :

`aws lambda get-policy --function-name {{nom}}`

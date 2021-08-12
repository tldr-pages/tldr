# aws lambda

> CLI pentru AWS lambda.
> Mai multe informaţii: <https://docs.aws.amazon.com/cli/latest/reference/lambda/>

- Rulează o funcție:

`aws lambda invoke --function-name {{name}} {{path/to/response}}.json`

- Rulați o funcție cu o sarcină utilă de intrare în format JSON:

`aws lambda invoke --function-name {{name}} --payload {{json}} {{path/to/response}}.json`

- Funcţii de listă:

`aws lambda list-functions`

- Afișează configurația unei funcții:

`aws lambda get-function-configuration --function-name {{name}}`

- Funcția listă pseudonime:

`aws lambda list-aliases --function-name {{name}}`

- Afișează configurația concurentă rezervată pentru o funcție:

`aws lambda get-function-concurrency --function-name {{name}}`

- Lista serviciilor AWS pot invoca funcția:

`aws lambda get-policy --function-name {{name}}`

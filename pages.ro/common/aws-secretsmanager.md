# aws secretsmanager

> Stocați, gestionați și regăsiți secrete.
> Mai multe informaţii: <https://docs.aws.amazon.com/cli/latest/reference/secretsmanager/>

- Arată secretele stocate de managerul secretelor în contul curent:

`aws secretsmanager list-secrets`

- Creează un secret:

`aws secretsmanager create-secret --name {{name}} --description "{{secret_description}}" --secret-string {{secret}}`

- Şterge un secret:

`aws secretsmanager delete-secret --secret-id {{name_or_arn}}`

- Vezi detaliile unui secret, cu excepția textului secret:

`aws secretsmanager describe-secret --secret-id {{name_or_arn}}`

- Recuperați valoarea unui secret (pentru a obține cea mai recentă versiune a omiterii secrete `—versiune`):

`aws secretsmanager get-secret-value --secret-id {{name_or_arn}} --version-stage {{version_of_secret}}`

- Rotiți secretul imediat folosind o funcție Lambda:

`aws secretsmanager rotate-secret --secret-id {{name_or_arn}} --rotation-lambda-arn {{arn_of_lambda_function}}`

- Rotiți secretul automat la fiecare 30 de zile folosind o funcție Lambda:

`aws secretsmanager rotate-secret --secret-id {{name_or_arn}} --rotation-lambda-arn {{arn_of_lambda_function}} --rotation-rules AutomaticallyAfterDays={{30}}`

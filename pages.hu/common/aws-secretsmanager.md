# aws secretsmanager

> Titkok tárolása, kezelése és visszakeresése. További információ: <https://docs.aws.amazon.com/cli/latest/reference/secretsmanager/>.

- A titkok kezelője által az aktuális fiókban tárolt titkok megjelenítése:

`aws secretsmanager list-secrets`

- Titok létrehozása:

`aws secretsmanager create-secret --name {{name}} --description "{{secret_description}}" --secret-string {{secret}}`

- Titok törlése:

`aws secretsmanager delete-secret --secret-id {{name_or_arn}}`

- A titok részleteinek megtekintése a titkos szöveg kivételével:

`aws secretsmanager describe-secret --secret-id {{name_or_arn}}`

- Egy titok értékének lekérdezése (a titok legfrissebb verziójának lekérdezéséhez hagyja ki a `--version-stage`):

`aws secretsmanager get-secret-value --secret-id {{name_or_arn}} --version-stage {{version_of_secret}}`

- A titok azonnali forgatása egy Lambda függvény segítségével:

`aws secretsmanager rotate-secret --secret-id {{name_or_arn}} --rotation-lambda-arn {{arn_of_lambda_function}}`

- A titok automatikus forgatása 30 naponként egy Lambda-függvény segítségével:

`aws secretsmanager rotate-secret --secret-id {{name_or_arn}} --rotation-lambda-arn {{arn_of_lambda_function}} --rotation-rules AutomaticallyAfterDays={{30}}`

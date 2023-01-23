# aws

> Az Amazon Web Services hivatalos CLI-eszköze. Egyes alparancsok, például a `aws s3` saját használati dokumentációval rendelkeznek. További információk: <https://aws.amazon.com/cli>.

- Az AWS parancssorának konfigurálása:

`aws configure wizard`

- Az AWS parancssor konfigurálása SSO használatával:

`aws configure sso`

- Lásd az AWS parancs súgószövegét:

`aws {{command}} help`

- A hívó személyazonosságának lekérdezése (a jogosultságok hibakereséséhez használatos):

`aws sts get-caller-identity`

- AWS-erőforrások listázása egy régióban és kimenet YAML-ben:

`aws dynamodb list-tables --region {{us-east-1}} --output yaml`

- Automatikus prompt használata a parancsok segítésére:

`aws iam create-user --cli-auto-prompt`

- Interaktív varázsló lekérése egy AWS-erőforráshoz:

`aws dynamodb wizard {{new_table}}`

- JSON CLI-csontváz generálása (hasznos az infrastruktúra kódként történő felhasználásához):

`aws dynamodb update-table --generate-cli-skeleton`

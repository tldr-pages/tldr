# aws

> Il tool da linea di comando ufficiale per Amazon Web Services.
> Alcuni sottocomandi, come `s3`, hanno la propria documentazione.
> Maggiori informazioni: <https://docs.aws.amazon.com/cli/latest/reference/>.

- Configura l'AWS Command Line tramite procedura guidata:

`aws configure wizard`

- Configura l'AWS Command Line usando SSO:

`aws configure sso`

- Mostra l'identità del chiamante (utile per diagnosticare problemi di permessi):

`aws sts get-caller-identity`

- Elenca le tabelle DynamoDB in una regione e mostra l'output in YAML:

`aws dynamodb list-tables --region {{us-east-1}} --output yaml`

- Usa il prompt automatico per aiutare nella compilazione di un comando:

`aws iam create-user --cli-auto-prompt`

- Avvia una procedura guidata interattiva per una risorsa AWS:

`aws dynamodb wizard {{new_table}}`

- Genera uno scheletro JSON per il CLI (utile per infrastruttura come codice):

`aws dynamodb update-table --generate-cli-skeleton`

- Mostra la pagina di aiuto per uno specifico comando:

`aws {{comando}} help`

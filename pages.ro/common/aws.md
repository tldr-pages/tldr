# aws

> Instrumentul oficial CLI pentru Amazon Web Services.
> Opțiunile Expert, SSO, Completare automată resurse și YAML sunt numai v2.
> Mai multe informaţii: <https://aws.amazon.com/cli>

- Configurați linia de comandă AWS:

`aws configure wizard`

- Configurați linia de comandă AWS utilizând SSO:

`aws configure sso`

- Consultați textul de ajutor pentru comanda AWS:

`aws {{command}} help`

- Obțineți identitatea apelantului (utilizată pentru depanarea permisiunilor):

`aws sts get-caller-identity`

- Lista resurselor AWS într-o regiune și de ieșire în yaml:

`aws dynamodb list-tables --region {{us-east-1}} --output yaml`

- Utilizați linia automată pentru a vă ajuta cu o comandă:

`aws iam create-user --cli-auto-prompt`

- Obțineți un expert interactiv pentru o resursă AWS:

`aws dynamodb wizard {{new_table}}`

- Generarea unui schelet JSON CLI (util pentru infrastructură ca cod):

`aws dynamodb update-table --generate-cli-skeleton`

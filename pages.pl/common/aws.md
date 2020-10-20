# aws

> Oficjalne narzędzie CLI dla Amazon Web Services.
> Wizard, SSO, Resource Autocompletion, i opcje YAML są tylko v2.
> Więcej informacji: <https://aws.amazon.com/cli>.

- Konfiguruj AWS Command Line:

`aws configure wizard`

- Konfiguruj AWS Command Line używając SSO:

`aws configure sso`

- Zobacz tekst pomocy dla polecenia AWS:

`aws {{komenda}} help`

- Uzyskaj tożsamość wywołującego (służy do rozwiązywania problemów z uprawnieniami):

`aws sts get-caller-identity`

- Wyświetla listę zasobów AWS w regionie i wyświetla w yaml:

`aws dynamodb list-tables --region {{us-east-1}} --output yaml`

- Użyj auto prompt do pomocy z poleceniem:

`aws iam create-user --cli-auto-prompt`

- Uzyskaj interaktywnego kreatora dla zasobu AWS:

`aws dynamodb wizard {{nowa_tabela}}`

- Generuj JSON CLI Skeleton (przydatne dla infrastruktury jako kodu):

`aws dynamodb update-table --generate-cli-skeleton`

# aws

> Oficjalne narzędzie CLI dla Amazon Web Services.
> Niektóre podkomendy takie jak `s3` mają osobną dokumentację.
> Więcej informacji: <https://aws.amazon.com/cli>.

- Konfiguruj AWS Command-line:

`aws configure wizard`

- Konfiguruj AWS Command-line używając SSO:

`aws configure sso`

- Uzyskaj tożsamość wywołującego (służy do rozwiązywania problemów z uprawnieniami):

`aws sts get-caller-identity`

- Uzyskaj listę zasobów AWS w regionie i wyświetl ją w YAML:

`aws dynamodb list-tables --region {{us-east-1}} --output yaml`

- Użyj auto prompt do pomocy z poleceniem:

`aws iam create-user --cli-auto-prompt`

- Uzyskaj interaktywnego kreatora dla zasobu AWS:

`aws dynamodb wizard {{nowa_tabela}}`

- Generuj JSON CLI Skeleton (przydatne dla infrastruktury jako kodu):

`aws dynamodb update-table --generate-cli-skeleton`

- Wyświetl pomoc dla określonej komendy:

`aws {{komenda}} help`

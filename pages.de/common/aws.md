# aws

> Das offiziellen Kommandozeilen Werkzeug für Amazon Web Services.
> Ausführungssassistent, SSO, Autovervollständigung von Ressourcen sowie YAML Optionen sind nur unter Version v2 verfügbar.
> Mehr Informationen: <https://aws.amazon.com/cli>.

- Konfigurieren der AWS Kommandozeile:

`aws configure wizard`

- Konfigurieren der AWS Kommandozeile mit Hilfe von SSO:

`aws configure sso`

- Anzeigen der Hilfe für ein Kommando:

`aws {{command}} help`

- Detail-Auflistung der eigenen angenommen Identität (häufig benutzt für die Fehlersuche):

`aws sts get-caller-identity`

- Auflistung aller AWS Ressourcen in einer Region mit YAML Formatierung:

`aws dynamodb list-tables --region {{us-east-1}} --output yaml`

- Erstellen eines IAM Benutzers mit Ausführungsassistent:

`aws iam create-user --cli-auto-prompt`

- Öffnen eines Assitenten für eine AWS Ressource:

`aws dynamodb wizard {{new-table}}`

- Erstellung eines JSON Kommandozeilen-Aufbaus (hilfreich für Infrastruktur Automation):

`aws dynamodb update-table --generate-cli-skeleton`

# aws cloud9

> Gestisce Cloud9 - una raccolta di strumenti per codificare, costruire, eseguire, testare, debuggare e rilasciare software nel cloud.
> Maggiori informazioni: <https://docs.aws.amazon.com/cli/latest/reference/cloud9/>.

- Elenca tutti gli identificativi degli ambienti di sviluppo Cloud9:

`aws cloud9 list-environments`

- Crea un ambiente di sviluppo Cloud9:

`aws cloud9 create-environment-ec2 --name {{nome}} --instance-type {{tipo_istanza}}`

- Visualizza informazioni sugli ambienti di sviluppo Cloud9:

`aws cloud9 describe-environments --environment-ids {{ids_environment}}`

- Aggiunge un membro ambiente a un ambiente di sviluppo Cloud9:

`aws cloud9 create-environment-membership --environment-id {{id_environment}} --user-arn {{arn_utente}} --permissions {{permessi}}`

- Visualizza informazioni sullo stato di un ambiente di sviluppo Cloud9:

`aws cloud9 describe-environment-status --environment-id {{id_environment}}`

- Elimina un ambiente Cloud9:

`aws cloud9 delete-environment --environment-id {{id_environment}}`

- Elimina un membro ambiente da un ambiente di sviluppo:

`aws cloud9 delete-environment-membership --environment-id {{id_environment}} --user-arn {{arn_utente}}`

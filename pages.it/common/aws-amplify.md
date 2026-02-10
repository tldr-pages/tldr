# aws amplify

> Piattaforma di sviluppo per la creazione di applicazioni mobile e web sicure e scalabili.
> Maggiori informazioni: <https://docs.aws.amazon.com/cli/latest/reference/amplify/>.

- Crea una nuova app Amplify:

`aws amplify create-app --name {{nome_app}} --description {{descrizione}} --repository {{repo_url}} --platform {{platform}} --environment-variables {{env_vars}} --tags {{tags}}`

- Elimina un'app Amplify esistente:

`aws amplify delete-app --app-id {{app_id}}`

- Ottieni dettagli di un'app Amplify specifica:

`aws amplify get-app --app-id {{app_id}}`

- Elenca tutte le app Amplify:

`aws amplify list-apps`

- Aggiorna le impostazioni di un'app Amplify:

`aws amplify update-app --app-id {{app_id}} --name {{nuovo_nome}} --description {{nuova_description}} --repository {{nuova_repo_url}} --environment-variables {{nuove_env_vars}} --tags {{nuove_tags}}`

- Aggiungi un nuovo ambiente backend a un'app Amplify:

`aws amplify create-backend-environment --app-id {{app_id}} --environment-name {{nome_env}} --deployment-artifacts {{artifacts}}`

- Rimuovi un ambiente backend da un'app Amplify:

`aws amplify delete-backend-environment --app-id {{app_id}} --environment-name {{nome_env}}`

- Elenca tutti gli ambienti backend in un'app Amplify:

`aws amplify list-backend-environments --app-id {{app_id}}`

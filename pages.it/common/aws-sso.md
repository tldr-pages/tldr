# aws sso

> Gestisce l'accesso alle risorse AWS utilizzando credenziali Single Sign-On (SSO).
> Maggiori informazioni: <https://docs.aws.amazon.com/cli/latest/reference/sso/>.

- Avvia sessione SSO e aggiorna i token di accesso. Richiede configurazione con `aws configure sso`:

`aws sso login`

- Termina sessione SSO e cancella i token di accesso memorizzati nella cache:

`aws sso logout`

- Elenca tutti gli account AWS accessibili all'utente:

`aws sso list-accounts`

- Elenca tutti i ruoli accessibili all'utente per un dato account AWS:

`aws sso list-account-roles --account-id {{account}} --access-token {{token}}`

- Recupera credenziali a breve termine per un account specifico:

`aws sso get-role-credentials --account-id {{account}} --role-name {{ruolo}} --access-token {{token}}`

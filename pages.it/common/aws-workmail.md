# aws workmail

> Gestisce Amazon WorkMail.
> Maggiori informazioni: <https://docs.aws.amazon.com/cli/latest/reference/workmail/>.

- Elenca tutte le organizzazioni WorkMail:

`aws workmail list-organizations`

- Elenca tutti gli utenti di un'organizzazione specifica:

`aws workmail list-users --organization-id {{id_organizzazione}}`

- Crea un utente WorkMail in un'organizzazione specifica:

`aws workmail create-user --name {{username}} --display-name {{name}} --password {{password}} --organization-id {{id_organizzazione}}`

- Registra e abilita un gruppo/utente per WorkMail:

`aws workmail register-to-work-mail --entity-id {{id_entita'}} --email {{email}} --organization-id {{id_organizzazione}}`

- Crea un gruppo WorkMail in un'organizzazione specifica:

`aws workmail create-group --name {{group_name}} --organization-id {{id_organizzazione}}`

- Associa un membro a un gruppo specifico:

`aws workmail associate-member-to-group --group-id {{group_id}} --member-id {{member_id}} --organization-id {{id_organizzazione}}`

- Deregistra e disabilita un utente/gruppo da WorkMail:

`aws workmail deregister-from-work-mail --entity-id {{id_entita'}} --organization-id {{id_organizzazione}}`

- Elimina un utente da un'organizzazione:

`aws workmail delete-user --user-id {{user_id}} --organization-id {{id_organizzazione}}`

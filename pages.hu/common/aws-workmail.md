# aws workmail

> Az Amazon WorkMail kezelése a CLI segítségével. További információk: <https://awscli.amazonaws.com/v2/documentation/api/latest/reference/workmail/index.html>.

- Az összes WorkMail szervezet listázása:

`aws workmail list-organizations`

- Egy adott szervezet összes felhasználójának listázása:

`aws workmail list-users --organization-id {{organization_id}}`

- WorkMail-felhasználó létrehozása egy adott szervezetben:

`aws workmail create-user --name {{username}} --display-name {{name}} --password {{password}} --organization-id {{organization_id}}`

- Csoport/felhasználó regisztrálása és engedélyezése a WorkMailhez:

`aws workmail register-to-work-mail --entity-id {{entity_id}} --email {{email}} --organization-id {{organization_id}}`

- WorkMail-csoport létrehozása egy adott szervezetben:

`aws workmail create-group --name {{group_name}} --organization-id {{organization_id}}`

- Tag hozzárendelése egy adott csoporthoz:

`aws workmail associate-member-to-group --group-id {{group_id}} --member-id {{member_id}} --organization-id {{organization_id}}`

- Felhasználó/csoport törlése és letiltása a WorkMailből:

`aws workmail deregister-from-work-mail --entity-id {{entity_id}} --organization-id {{organization_id}}`

- Felhasználó törlése egy szervezetből:

`aws workmail delete-user --user-id {{user_id}} --organization-id {{organization_id}}`

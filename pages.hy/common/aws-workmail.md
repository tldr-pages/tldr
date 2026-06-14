# aws աշխատանքային փոստ

> Կառավարեք Amazon WorkMail-ը:.
> Լրացուցիչ տեղեկություններ. <https://docs.aws.amazon.com/cli/latest/reference/workmail/>:.

- Թվարկեք բոլոր WorkMail կազմակերպությունները.:

`aws workmail list-organizations`

- Նշեք կոնկրետ կազմակերպության բոլոր օգտվողներին.:

`aws workmail list-users --organization-id {{organization_id}}`

- Ստեղծեք WorkMail օգտվող կոնկրետ կազմակերպությունում.:

`aws workmail create-user --name {{username}} --display-name {{name}} --password {{password}} --organization-id {{organization_id}}`

- Գրանցեք և միացրեք խումբ/օգտատեր WorkMail-ում.:

`aws workmail register-to-work-mail --entity-id {{entity_id}} --email {{email}} --organization-id {{organization_id}}`

- Ստեղծեք WorkMail խումբ կոնկրետ կազմակերպությունում.:

`aws workmail create-group --name {{group_name}} --organization-id {{organization_id}}`

- Ասոցացնել անդամին որոշակի խմբի.:

`aws workmail associate-member-to-group --group-id {{group_id}} --member-id {{member_id}} --organization-id {{organization_id}}`

- Չգրանցել և անջատել օգտվողին/խումբին WorkMail-ից.:

`aws workmail deregister-from-work-mail --entity-id {{entity_id}} --organization-id {{organization_id}}`

- Ջնջել օգտվողին կազմակերպությունից.:

`aws workmail delete-user --user-id {{user_id}} --organization-id {{organization_id}}`

# kcadm.sh

> Կատարել կառավարման առաջադրանքներ:.
> Լրացուցիչ տեղեկություններ. <https://www.keycloak.org/docs/latest/server_admin/#admin-cli>:.

- Սկսեք վավերացված նստաշրջան.:

`kcadm.sh config credentials --server {{host}} --realm {{realm_name}} --user {{username}} --password {{password}}`

- Ստեղծեք օգտվող.:

`kcadm.sh create users -s username={{username}} -r {{realm_name}}`

- Թվարկեք բոլոր ոլորտները.:

`kcadm.sh get realms`

- Թարմացրեք ոլորտը JSON կազմաձևով.:

`kcadm.sh update realms/{{realm_name}} -f {{path/to/file.json}}`

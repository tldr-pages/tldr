# kcadm.sh

> Adminisztrációs feladatok végrehajtása a parancssori felületről (CLI). További információ: <https://www.keycloak.org/docs/latest/server_admin/#admin-cli>.

- Hitelesített munkamenet indítása:

`kcadm.sh config credentials --server {{host}} --realm {{realm_name}} --user {{username}} --password {{password}}`

- Hozzon létre egy felhasználót:

`kcadm.sh create users -s username={{username}} -r {{realm_name}}`

- Az összes birodalom listázása:

`kcadm.sh get realms`

- Egy birodalom frissítése JSON konfigurációval:

`kcadm.sh update realms/{{realm_name}} -f {{path/to/file.json}}`

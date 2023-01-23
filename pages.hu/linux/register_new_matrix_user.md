# register_new_matrix_user

> Új felhasználók regisztrálására szolgál egy adott háziszerveren, ha a regisztráció le van tiltva. További információ: <https://manned.org/register_new_matrix_user>.

- Felhasználó létrehozása interaktívan:

`register_new_matrix_user --config {{path/to/homeserver.yaml}}`

- Admin felhasználó létrehozása interaktívan:

`register_new_matrix_user --config {{path/to/homeserver.yaml}} --admin`

- Admin felhasználó létrehozása nem interaktív módon (nem ajánlott):

`register_new_matrix_user --config {{path/to/homeserver.yaml}} --user {{username}} --password {{password}} --admin`

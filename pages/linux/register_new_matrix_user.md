# register_new_matrix_user

> Register new users in a home server when registration has been disabled.
> More information: <https://manned.org/register_new_matrix_user>.

- Create a user interactively:

`register_new_matrix_user --config {{path/to/homeserver.yaml}}`

- Create an admin user interactively:

`register_new_matrix_user --config {{path/to/homeserver.yaml}} --admin`

- Create an admin user non-interactively (not recommended):

`register_new_matrix_user --config {{path/to/homeserver.yaml}} --user {{username}} --password {{password}} --admin`

# marzban cli

> Manage administrators, users, and subscriptions.
> More information: <https://github.com/Gozargah/Marzban/blob/master/cli/README.md>.

- List all administrators:

`marzban cli admin list`

- Create a new administrator:

`marzban cli admin create {{[-u|--username]}} {{username}}`

- List all users:

`marzban cli user list`

- Transfer ownership of a user to another administrator:

`marzban cli user set-owner {{[-u|--username]}} {{username}} --owner {{owner}}`

- Generate a subscription configuration for a user:

`marzban cli subscription get-config {{[-u|--username]}} {{username}} {{[-f|--format]}} {{v2ray|clash}}`

- Display a user's subscription link:

`marzban cli subscription get-link {{[-u|--username]}} {{username}}`

- Display help:

`marzban cli --help`

# marzban cli

> Manage Marzban via the command line interface.
> More information: <https://github.com/Gozargah/Marzban/blob/master/cli/README.md>.

- Show help for the CLI:

`marzban cli --help`

- List all administrators:

`marzban cli admin list`

- Create a new administrator:

`marzban cli admin create --username {{username}}`

- List all users:

`marzban cli user list`

- Transfer ownership of a user to another administrator:

`marzban cli user set-owner --username {{username}} --owner {{owner}}`

- Generate a subscription configuration for a user:

`marzban cli subscription get-config --username {{username}} --format {{v2ray|clash}}`

- Display a user's subscription link:

`marzban cli subscription get-link --username {{username}}`

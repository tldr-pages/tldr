# pass-cli

> Access and manage Proton Pass vaults and items.
> More information: <https://protonpass.github.io/pass-cli/commands/login/>.

- Log in using the default web flow:

`pass-cli login`

- Display information about the current session:

`pass-cli info`

- List vaults:

`pass-cli vault list`

- List items in a specific vault:

`pass-cli item list "{{vault_name}}"`

- View a specific item by title in a vault:

`pass-cli item view --vault-name "{{vault_name}}" --item-title "{{item_title}}"`

- Log out of the current session:

`pass-cli logout`

- Display help:

`pass-cli --help`

- Display version:

`pass-cli --version`

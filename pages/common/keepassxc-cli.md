# keepassxc-cli

> Command-line interface for KeepassXC.
> More information: <https://manned.org/keepassxc-cli>.

- Search entries:

`keepassxc-cli lookup {{path/to/database_file}} {{name}}`

- List the contents of a folder:

`keepassxc-cli ls {{path/to/database_file}} {{/path/to/directory}}`

- Add an entry with an auto-generated password:

`keepassxc-cli add --generate {{path/to/database_file}} {{entry_name}}`

- Delete an entry:

`keepassxc-cli rm {{path/to/database_file}} {{entry_name}}`

- Copy an entry's password to the clipboard:

`keepassxc-cli clip {{path/to/database_file}} {{entry_name}}`

- Copy a TOTP code to the clipboard:

`keepassxc-cli clip --totp {{path/to/database_file}} {{entry_name}}`

- Generate a passphrase with 7 words:

`keepassxc-cli diceware --words {{7}}`

- Generate a password with 16 printable ASCII characters:

`keepassxc-cli generate --lower --upper --numeric --special --length {{16}}`

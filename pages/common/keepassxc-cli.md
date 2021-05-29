# keepassxc-cli

> Command Line interface for the keepassxc app.
> More information: <https://keepassxc.org/>.

- Search entries:

`keepassxc-cli lookup {{database_file}} {{name}}`

- List a folder:

`keepassxc-cli ls {{database_file}} {{folder_name}}`

- Add entry with auto-generated password:

`keepassxc-cli add -g {{database_file}} {{entry_name}}`

- Generate a char password with lower and upper cases, numbers and special characters:

`keepassxc-cli generate -lUns -L {{16}}`

- Generate a passphrase with `7` words:

`keepassxc-cli diceware -W {{7}}`

- Copy an entry's password to the clipboard:

`keepassxc-cli clip {{database_file}} {{entry_name}}`

- Copy TOTP to the clipboard:

`keepassxc-cli clip -t {{database_file}} {{entry_name}}`

- Delete an entry :

`keepassxc-cli rm {{database_file}} {{entry_name}}`

# pass

> Tool for storing and reading passwords or other sensitive data.
> All data is GPG-encrypted, and managed with a Git repository.
> More information: <https://www.passwordstore.org>.

- Initialize (or re-encrypt) the storage using one or more GPG IDs:

`pass init {{gpg_id_1}} {{gpg_id_2}}`

- Save a new password and additional information (press Ctrl + D on a new line to complete):

`pass insert --multiline {{path/to/data}}`

- Edit an entry:

`pass edit {{path/to/data}}`

- Copy a password (first line of the data file) to the clipboard:

`pass -c {{path/to/data}}`

- List the whole store tree:

`pass`

- Generate a new random password with a given length, and copy it to the clipboard:

`pass generate -c {{path/to/data}} {{num}}`

- Initialize a new Git repository (any changes done by pass will be committed automatically):

`pass git init`

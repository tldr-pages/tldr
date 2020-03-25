# pass

> Tool for storing and reading passwords or other sensitive data.
> All data is GPG-encrypted, and managed with a git repository.
> More information: <https://www.passwordstore.org>.

- Initialize the storage using a gpg-id for encryption:

`pass init {{gpg_id}}`

- Save a new password (prompts you for the value without echoing it):

`pass insert {{path/to/data}}`

- Copy a password (first line of the data file) to the clipboard:

`pass -c {{path/to/data}}`

- List the whole store tree:

`pass`

- Generate a new random password with a given length, and copy it to the clipboard:

`pass generate -c {{path/to/data}} {{num}}`

- Run any git command against the underlying store repository:

`pass git {{git_arguments}}`

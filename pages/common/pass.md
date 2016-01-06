# pass

> safely store and read passwords or other sensitive data easily
> all data is GPG-encrypted, and managed with a git repository

- initialize the storage using a gpg-id for encryption

`pass init {{gpg_id}}`

- save a new password (prompts you for the value without echoing it)

`pass insert {{path/to/data}}`

- copy a password (first line of the data file) to the clipboard

`pass -c {{path/to/data}}`

- list the whole store tree

`pass`

- generate a new random password with a given length, and copy it to the clipboard

`pass generate -c {{path/to/data}} {{num}}`

- run any git command against the underlying store repository

`pass git {{git-arguments}}`

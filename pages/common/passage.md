# passage

> Store and read passwords or other sensitive data.
> Note: All data is age-encrypted (as opposed to GPG used by `pass`).
> More information: <https://github.com/FiloSottile/passage>.

- Insert a new password (press `<Ctrl d>` on a new line to complete):

`passage insert {{[-m|--multiline]}} {{path/to/data}}`

- Insert a new password from `stdin`:

`echo "{{password}}" | passage insert {{[-e|--echo]}} {{path/to/data}}`

- Show a password:

`passage {{path/to/data}}`

- Copy a password to the clipboard:

`passage {{[-c|--clip]}} {{path/to/data}}`

- List the whole store tree:

`passage ls`

- Generate a new random password of a given length:

`passage generate {{path/to/data}} {{length}}`

- Edit an entry:

`passage edit {{path/to/data}}`

- Remove an entry:

`passage rm {{path/to/data}}`

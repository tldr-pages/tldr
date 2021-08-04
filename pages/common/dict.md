# dict

> Command line dictionary using the DICT protocol.
> More information: <https://github.com/cheusov/dictd>.

- List available databases:

`dict -D`

- Get information about a database:

`dict -i {{database_name}}`

- Look up a word in a specific database:

`dict -d {{database_name}} {{word}}`

- Look up a word in all available databases:

`dict {{word}}`

- Show information about the DICT server:

`dict -I`

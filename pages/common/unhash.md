# unhash

> Remove some cached element from an internal hash table.
> See also: `hash`.
> More information: <https://fossies.org/linux/zsh/Doc/help/unhash>.

- Remove a command from the hash table:

`unhash {{command}}`

- Unhash non-suffix aliases:

`unhash -a {{alias}}`

- Unhash suffix aliases:

`unhash -s {{alias}}`

- Unhash shell functions:

`unhash -f {{function}}`

- Unhash directories:

`unhash -d {{directory}}`

- Unhash every function that matches a pattern:

`unhash -f -m "{{git*}}"`

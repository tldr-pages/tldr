# unhash

> Remove some cached element from an internal hash table.
> See also: `hash`.
> More information: <https://fossies.org/linux/zsh/Doc/help/unhash>.

- Remove a [c]ommand from the hash table:

`unhash {{command}}`

- Unhash non-suffix [a]liases:

`unhash -a {{alias}}`

- Unhash [s]uffix aliases:

`unhash -s {{alias}}`

- Unhash shell [f]unctions:

`unhash -f {{function}}`

- Unhash [d]irectories:

`unhash -d {{directory}}`

- Unhash every function that matches a pattern:

`unhash -f -m "{{git*}}"`

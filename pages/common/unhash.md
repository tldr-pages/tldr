# unhash

> Remove hashed executable locations.
> See also: `hash`.
> More information: <https://zsh.sourceforge.io/Doc/Release/Shell-Builtin-Commands.html>.

- Remove a specific command from the hash table:

`unhash {{command}}`

- Unhash non-suffix [a]liases:

`unhash -a {{alias}}`

- Unhash [s]uffix aliases:

`unhash -s {{alias}}`

- Unhash shell [f]unctions:

`unhash -f {{function}}`

- Unhash [d]irectories:

`unhash -d {{directory}}`

- Unhash every function that [m]atches a pattern:

`unhash -f -m "{{pattern}}"`

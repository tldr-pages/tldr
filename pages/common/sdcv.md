# sdcv

> StarDict, a command-line dictionary client.
> Dictionaries are provided separately from the client.
> More information: <https://manned.org/sdcv>.

- Start `sdcv` interactively:

`sdcv`

- List installed dictionaries:

`sdcv --list-dicts`

- Display a definition from a specific dictionary:

`sdcv --use-dict {{dictionary_name}} {{search_term}}`

- Look up a definition with a fuzzy search:

`sdcv {{search_term}}`

- Look up a definition with an exact search:

`sdcv --exact-search {{search_term}}`

- Look up a definition and format the output as JSON:

`sdcv --json {{search_term}}`

- Search for dictionaries in a specific directory:

`sdcv --data-dir {{path/to/directory}} {{search_term}}`

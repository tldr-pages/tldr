# sdcv

> StarDict command-line version, dictionary client.
> Dictionaries are provided separately from the client.
> More information: <https://manned.org/sdcv>.

- Start sdcv interactively:

`sdcv`

- List installed dictionaries:

`sdcv --list-dicts`

- Display a definition from a specific dictionary:

`sdcv --use-dict {{dictionary_name}} {{search_term}}`

- Lookup a definition with a fuzzy search:

`sdcv {{search_term}}`

- Lookup a definition with an exact search:

`sdcv --exact-search {{search_term}}`

- Lookup definition and get json output:

`sdcv -j {{search_term}}`

- Look in a specific directory for dictionaries:

`sdvc --data-dir {{path/to/directory}} {{search_term}}`

- Display help:

`sdcv --help`

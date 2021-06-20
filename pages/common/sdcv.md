# sdcv

> StarDict console version. Command line dictionary client.
> Dictionaries are provided separately.
> More information: <https://manned.org/sdcv>.

- Start sdcv interactively:

`sdcv`

- List installed dictionaries:

`sdcv --list-dictist-dicts`

- Display a definition from a specific dictionary:

`sdcv --use-dict {{dictionary_name}} {{search_term}}`

- Lookup definition with fuzzy search:

`sdcv {{search_term}}`

- Lookup definition with exact search:

`sdcv --exact-search {{search_term}}`

- Lookup definition and get json output:

`sdcv -j {{search_term}}`

- Look in specific directory for dictionaries:

`sdvc --data-dir {{path/to/directory}} {{search_term}}`

- Display help:

`sdcv --help`

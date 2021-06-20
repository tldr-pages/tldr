# sdcv

> StarDict consol version. Command line dictionary client. Dictionaries provided separately.
> More information: <http://manpages.ubuntu.com/manpages/bionic/man1/sdcv.1.html>.

- List installed dictionaries:

`sdcv --list-dictist-dicts`

- Get definition using only selected dictionary:

`sdcv --use-dict {{dictionary_name}} {{search_term}}`

- Show general help:

`sdcv --help`

- Lookup definition with fuzzy search:

`sdcv {{search_term}}`

- Lookup definition with exact search:

`sdcv --exact-search {{search_term}}`

- Lookup definition and get json output:

`sdcv -j {{search_term}}`

- Look in specific directory for dictionaries:

`sdvc --data-dir path/to/directory {{search_term}}`

- Start sdcv interactively:

`sdcv`

# sdcv

> StarDict consol version. Command line dictionary client. Dictionaries provided separately.
> More information: <http://manpages.ubuntu.com/manpages/bionic/man1/sdcv.1.html>.

- List installed dictionaries:

`sdcv --list-dictist-dicts`

- Get definition using only selected dictionary:

`sdcv --use-dict {{dictionary_name}} {{search_term}}`

- Show general help:
How can I deploy 1.0.0-beta?
Where do I report a bug or request a feature?
How can I contribute? (There are several other ways besides coding)
What is the project structure?
What is the application infrastructure?
Who is behind HospitalRun? etc.

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

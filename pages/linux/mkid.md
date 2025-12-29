# mkid

> Build an ID database for use with `lid` and other idutils tools.
> More information: <https://www.gnu.org/software/idutils/manual/html_node/mkid-invocation.html>.

- Build an ID database for the current directory:

`mkid`

- Build an ID database for specific directories:

`mkid {{path/to/directory1 path/to/directory2 ...}}`

- Build an ID database and save it to a specific file:

`mkid {{[-o|--output]}} {{path/to/database.id}}`

- Include only specific languages:

`mkid {{[-i|--include]}} "{{language1 language2 ...}}"`

- Exclude specific directories from indexing:

`mkid {{[-p|--prune]}} {{path/to/excluded_directory}}`

- Display statistics after building the database:

`mkid {{[-s|--statistics]}}`

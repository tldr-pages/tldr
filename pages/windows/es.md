# es

> Command-line interface for Everything, a fast file and folder search tool for Windows.
> Requires Everything to be installed and running in the background.
> More information: <https://www.voidtools.com/support/everything/command_line_interface/>.

- Search for a file or folder by name:

`es {{search_term}}`

- Search using a regular expression:

`es -r {{regex_pattern}}`

- Match whole words:

`es -w {{search_term}}`

- Limit the number of results shown:

`es -n {{10}} {{search_term}}`

- Search within a specific folder:

`es -path {{folder_path}} {{search_term}}`

- List folders only:

`es /ad`

- List files only:

`es /a-d`

- Sort results (e.g., by name):

`es -sort {{name-ascending}}`

# es
> Command-line interface for Everything, a fast file and folder search tool for Windows.
> Requires Everything to be installed and running in the background.
> More information: <https://www.voidtools.com/support/everything/command_line_interface/>.

- Search for a file or folder by name:

  `es {{search_term}}`

- Search using a regular expression:

  `es -r {{regex_pattern}}`

- Match whole words or case-sensitive searches:

  `es -w {{search_term}}`
  `es -i {{search_term}}`

- Limit the number of results shown:

  `es -n {{10}} {{search_term}}`

- Search within a specific folder or parent path:

  `es -path {{folder_path}} {{search_term}}`
  `es -parent-path {{parent_folder_path}} {{search_term}}`

- List folders only or files only:

  `es /ad`  # Folders only
  `es /a-d` # Files only

- Sort results (e.g., by name or size) in ascending or descending order:

  `es -sort {{name-ascending}}`
  `es -sort {{size-descending}}`

- Export search results to a file (CSV, TXT, etc.):

  `es -export-csv {{output.csv}} {{search_term}}`

- Display additional file properties (e.g., size, date modified):

  `es -size -date-modified {{search_term}}`

- Save the current Everything database to disk:

  `es -save-db`

- Display the version of Everything or `es`:

  `es -get-everything-version`
  `es -version`


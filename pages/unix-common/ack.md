# ack

> A search tool like `grep`, optimized for developers.
> See also: `rg`, which is much faster.
> More information: <https://beyondgrep.com/documentation>.

- Search for files containing a string or regular expression in the current directory recursively:

`ack "{{search_pattern}}"`

- Search for a case-insensitive pattern:

`ack --ignore-case "{{search_pattern}}"`

- Search for lines matching a pattern, printing [o]nly the matched text and not the rest of the line:

`ack -o "{{search_pattern}}"`

- Limit search to files of a specific type:

`ack --type {{ruby}} "{{search_pattern}}"`

- Do not search in files of a specific type:

`ack --type no{{ruby}} "{{search_pattern}}"`

- Count the total number of matches found:

`ack --count --no-filename "{{search_pattern}}"`

- Print the file names and the number of matches for each file only:

`ack --count --files-with-matches "{{search_pattern}}"`

- List all the values that can be used with `--type`:

`ack --help-types`

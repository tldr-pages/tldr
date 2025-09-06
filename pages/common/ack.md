# ack

> A search tool like `grep`, optimized for developers.
> See also: `rg`, which is much faster.
> More information: <https://beyondgrep.com/documentation>.

- Search for files containing a string or `regex` in the current directory recursively:

`ack "{{search_pattern}}"`

- Search for a case-insensitive pattern:

`ack {{[-i|--ignore-case]}} "{{search_pattern}}"`

- Search for lines matching a pattern, printing only the matched text and not the rest of the line:

`ack {{[-o|--output '$&']}} "{{search_pattern}}"`

- Limit search to files of a specific type:

`ack {{[-t|--type]}} {{ruby}} "{{search_pattern}}"`

- Do not search in files of a specific type:

`ack {{[-t|--type]}} no{{ruby}} "{{search_pattern}}"`

- Count the total number of matches found:

`ack {{[-c|--count]}} {{[-h|--no-filename]}} "{{search_pattern}}"`

- Print the file names and the number of matches for each file only:

`ack {{[-c|--count]}} {{[-l|--files-with-matches]}} "{{search_pattern}}"`

- List all the values that can be used with `--type`:

`ack --help-types`

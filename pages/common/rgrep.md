# rgrep

> Recursively find patterns in files using `regex`.
> Equivalent to `grep -r`.
> More information: <https://www.gnu.org/software/grep/manual/grep.html#Command_002dline-Options>.

- Recursively search for a pattern in the current working directory:

`rgrep "{{search_pattern}}"`

- Recursively search for a case-insensitive pattern in the current working directory:

`rgrep {{[-i|--ignore-case]}} "{{search_pattern}}"`

- Recursively search for an extended `regex` pattern (supports `?`, `+`, `{}`, `()` and `|`) in the current working directory:

`rgrep {{[-E|--extended-regexp]}} "{{search_pattern}}"`

- Recursively search for an exact string (disables `regex`) in the current working directory:

`rgrep {{[-F|--fixed-strings]}} "{{exact_string}}"`

- Recursively search for a pattern in a specified directory (or file):

`rgrep "{{search_pattern}}" {{path/to/file_or_directory}}`

# fastmod

> A fast partial replacement for the codemod tool, replace and replace all in the whole codebase.
> Regexes are matched by Rust regex crate.
> More information: <https://github.com/facebookincubator/fastmod>.

- Replace a `regex` in all files of the current directory, ignoring files on .ignore and .gitignore:

`fastmod {{regex}} {{replacement}}`

- Replace a `regex` in case-insensitive mode in specific files or directories:

`fastmod --ignore-case {{regex}} {{replacement}} -- {{path/to/file_or_directory1 path/to/file_or_directory2 ...}}`

- Replace a `regex` in a specific directory in files filtered with a case-insensitive glob pattern:

`fastmod {{regex}} {{replacement}} --dir {{path/to/directory}} --iglob '{{**/*.{js,json}}}'`

- Replace for an exact string in `.js` or JSON files:

`fastmod --fixed-strings {{exact_string}} {{replacement}} --extensions {{json,js}}`

- Replace for an exact string without prompt for a confirmation (disables `regex`):

`fastmod --accept-all --fixed-strings {{exact_string}} {{replacement}}`

- Replace for an exact string without prompt for a confirmation, printing changed files:

`fastmod --accept-all --print-changed-files --fixed-strings {{exact_string}} {{replacement}}`

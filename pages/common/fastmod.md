# fastmod

> A fast partial replacement for the codemod tool, replace and replace all in the whole codebase.
> Regexes are matched by Rust regex crate.
> More information: <https://github.com/facebookincubator/fastmod>.

- Replace a regex pattern in all files of the current directory, ignoring files on .ignore and .gitignore:

`fastmod {{regex_pattern}} {{replacement}}`

- Replace a regex pattern in case-insensitive mode in specific files or directories:

`fastmod --ignore-case {{regex_pattern}} {{replacement}} -- {{path/to/file path/to/directory ...}}`

- Replace a regex pattern in a specific directory in files filtered with a case-insensitive glob pattern:

`fastmod {{regex}} {{replacement}} --dir {{path/to/directory}} --iglob {{'**/*.{js,json}'}}`

- Replace for an exact string in .js or .json files:

`fastmod --fixed-strings {{exact_string}} {{replacement}} --extensions {{json,js}}`

- Replace for an exact string without prompt for a confirmation (disables regular expressions):

`fastmod --accept-all --fixed-strings {{exact_string}} {{replacement}}`

- Replace for an exact string without prompt for a confirmation, printing changed files:

`fastmod --accept-all --print-changed-files --fixed-strings {{exact_string}} {{replacement}}`

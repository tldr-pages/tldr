# fastmod

> A fast partial replacement for the codemod tool, replace and replace all in the whole codebase.
> Regexes are matched by Rust regex crate.
> More information: <https://github.com/facebookincubator/fastmod>.

- Replace regex pattern in current directory in all files, ignoring files on .ignore and .gitignore:

`fastmod {{regex_pattern}} {{replacement}}`

- Replace a regex pattern in all file in a specific directory:

`fastmod {{regex}} {{replacement}} -d {{src/}} --iglob {{'**/*.{js,json}'}}`

- Replace fixed non-regex string in .js or .json files:

`fastmod -F {{match}} {{replacement}} -e {{json,js}}`

- Replace all with non-regex string and without prompt for a confirmation:

`fastmod --accept-all -F {{match}} {{replacement}}`

- Replace all like previous example, and print changed files:

`fastmod --accept-all --print-changed-files -F {{match}} {{replacement}}`

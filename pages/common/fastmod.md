# fastmod

> A fast partial replacement for the codemod tool, replace and replace all in the whole codebase.
> Regexes are match with the regex crate: <https://crates.io/crates/regex>.
> More information: <https://github.com/facebookincubator/fastmod>.

- Replace regex pattern:

`fastmod {{regex_pattern}} {{replacement}} -d {{dir}} --iglob {{wildcard_patterns}}`

- Replace fixed string as it is (not regex), .js or .json files only:

`fastmod -F {{match_string}} {{replacement_string}} -e json,js`

- Replace-all without confirmation, replace string as it is (not regex):

`fastmod --accept-all -F {{match_string}} {{replacement_string}}`

- Replace-all similar to the above, but print changed files as well:

`fastmod --accept-all --print-changed-files -F {{match_string}} {{replacement_string}}`

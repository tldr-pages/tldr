# conan-search

> Search for package recipes in all the configured remotes, or in a specific one.
> More information: <https://docs.conan.io/2/reference/commands/search.html>.

- Search for a recipe in all remotes:

`conan search {{recipe}}`

- Search for all versions of a recipe:

`conan search {{recipe}}/*`

- Search in a specific remote only:

`conan search {{recipe}} --remote {{remote}}`

- Search in the remotes whose names match a pattern:

`conan search {{recipe}} --remote "{{remote_pattern}}"`

- Output the results as JSON to a file:

`conan search {{recipe}} --format json --out-file {{results.json}}`

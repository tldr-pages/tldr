# npm query

> Print an array of dependency objects using CSS-like selectors.
> More information: <https://docs.npmjs.com/cli/v8/commands/npm-query>.

- Print direct dependencies:

`npm query ':root > *'`

- Print all direct production/development dependencies:

`npm query ':root > .{{prod|dev}}'`

- Print dependencies with a specific name:

`npm query '#{{package}}'`

- Print dependencies with a specific name and within a semantic versioning range:

`npm query #{{package}}@{{semantic_version}}`

- Print dependencies which have no dependencies:

`npm query ':empty'`

- Find all dependencies with postinstall scripts and uninstall them:

`npm query ":attr(scripts, [postinstall])" | jq 'map(.name) | join("\n")' -r | xargs -I {} npm uninstall {}`

- Find all Git dependencies and print which application requires them:

`npm query ":type(git)" | jq 'map(.name)' | xargs -I {} npm why {}`

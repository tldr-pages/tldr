# npm unpublish

> Remove a package from the npm registry.
> More information: <https://docs.npmjs.com/cli/npm-unpublish>.

- Unpublish a specific package version:

`npm unpublish {{package_name}}@{{version}}`

- Unpublish the entire package:

`npm unpublish {{package_name}} {{[-f|--force]}}`

- Unpublish a package that is scoped:

`npm unpublish @{{scope}}/{{package_name}}`

- Specify a timeout period before unpublishing:

`npm unpublish {{package_name}} --timeout {{time_in_milliseconds}}`

- Dry run to see what would be unpublished without actually doing it:

`npm unpublish {{package_name}} --dry-run`

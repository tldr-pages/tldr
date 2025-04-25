# npm unpublish

> Remove a package from the npm registry.
> More information: <https://docs.npmjs.com/cli/commands/npm-unpublish>.

- Unpublish a specific package version:

`npm unpublish {{package_name}}@{{version}}`

- Unpublish the entire package:

`npm unpublish {{package_name}} {{[-f|--force]}}`

- Unpublish a package that is scoped:

`npm unpublish @{{scope}}/{{package_name}}`

- Specify a timeout period before unpublishing:

`npm unpublish {{package_name}} --timeout {{time_in_milliseconds}}`

- To prevent accidental unpublishing, use the `--dry-run` flag to see what would be unpublished:

`npm unpublish {{package_name}} --dry-run`

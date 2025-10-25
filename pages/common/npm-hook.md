# npm hook

> Manage npm registry hooks for packages.
> Note: This command has been deprecated.
> More information: <https://docs.npmjs.com/cli/v10/hook>.

- List all active hooks:

`npm hook ls`

- Add a new hook for a package:

`npm hook add {{package_name}} {{event}} {{target_url}}`

- Remove a specific hook by its ID:

`npm hook rm {{hook_id}}`

- Update a hook with new information:

`npm hook update {{hook_id}} {{target_url}}`

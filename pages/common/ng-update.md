# ng update

> Update an Angular workspace and its dependencies.
> More information: <https://angular.dev/cli/update>.

- Update all dependencies in the workspace:

`ng update`

- Update a specific package:

`ng update {{package}}`

- Update multiple packages:

`ng update {{package1 package2 ...}}`

- Ignore peer dependency version mismatches:

`ng update {{package}} --force`

- Allow updating when the repository contains modified or untracked files:

`ng update {{package}} --allow-dirty`

- Update to prerelease versions, including beta and release candidates:

`ng update {{package}} --next`

- Display additional details about internal operations:

`ng update {{package}} --verbose`

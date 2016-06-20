# equery

> View information about portage packages.

- List all installed packages:

`equery list '*'`

- Search for installed packages:

`equery list -po {{package_name}}`

- List all packages depending on a package:

`equery depends {{package_name}}`

- List package dependencies:

`equery depgraph {{package_name}}`

- List all files installed by a package:

`equery files --tree {{package_name}}`

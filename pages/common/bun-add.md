# bun add

> Modern JavaScript runtime, package manager, bundler, and test runner.
> More information: <https://bun.com/docs>.

- Install a single package:

`bun add {{package}}`

- Install multiple packages:

`bun add {{package1}} {{package2}}`

- Install from a Git repository:

`bun add {{git_url}}`

- Install a specific version:

`bun add {{package}}@{{version}}`

- Install from local file or directory:

`bun add file:{{path/to/file_or_directory}}`

- Add a dev dependency:

`bun add {{[-d|--dev]}} {{package}}`

- Add a package globally:

`bun add {{[-g|--global]}} {{package}}`

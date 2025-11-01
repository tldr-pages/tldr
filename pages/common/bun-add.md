# bun add

> Modern JavaScript runtime, package manager, bundler, and test runner.
> More information: <https://bun.com/docs>.

- Install a single package:

`bun {{[a|add]}} {{package}}`

- Install multiple packages:

`bun {{[a|add]}} {{package1}} {{package2}}`

- Install from a Git repository:

`bun {{[a|add]}} {{git_url}}`

- Install a specific version:

`bun {{[a|add]}} {{package}}@{{version}}`

- Install from local file or directory:

`bun {{[a|add]}} file:{{path/to/file_or_directory}}`

- Add a dev dependency:

`bun {{[a|add]}} {{[-d|--dev]}} {{package}}`

- Add a package globally:

`bun {{[a|add]}} {{[-g|--global]}} {{package}}`

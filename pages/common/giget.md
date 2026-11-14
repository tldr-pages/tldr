# giget

> Download project templates and extract subdirectories from git repositories.
> More information: <https://github.com/unjs/giget>.

- Clone a template from a GitHub repository into a target directory:

`giget {{gh:owner/repository}} {{path/to/directory}}`

- Clone a specific subdirectory and branch from a repository:

`giget {{gh:owner/repository/subdirectory#branch}} {{path/to/directory}}`

- Overwrite existing files in the destination directory:

`giget {{gh:owner/repository}} {{path/to/directory}} --force`

- Automatically install dependencies after downloading the template:

`giget {{gh:owner/repository}} {{path/to/directory}} --install`

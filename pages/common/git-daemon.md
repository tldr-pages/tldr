# git daemon

> A really simple server for Git repositories.
> More information: <https://git-scm.com/docs/git-daemon>.

- Launch a Git daemon with a whitelisted set of directories:

`git daemon --export-all {{path/to/directory1}} {{path/to/directory2}}`

- Launch a Git daemon with a specific base directory and allow pulling from all sub-directories that look like Git repositories:

`git daemon --base-path={{path/to/directory}} --export-all --reuseaddr`

- Launch a Git daemon with a base directory with allowed push access and verbosity:

`git daemon --base-path={{path/to/directory}} --export-all --enable=receive-pack --reuseaddr --informative-errors --verbose`

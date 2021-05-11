# git daemon

> A really simple server for Git repositories.
> More information: <https://git-scm.com/docs/git-daemon>.

- Git daemon with a whitelisted set of directories:

`git daemon --export-all {{path/to/directory1}} {{path/to/directory2}}`

- Git daemon with a base directory and allow pulling from all directories that look like Git repos:

`git daemon --base-path={{path/to/directory}} --export-all --reuseaddr`

- Git daemon with a base direcotry with allowed push access and verbosity:

 `git daemon --base-path={{path/to/directory}} --export-all --enable=receive-pack --reuseaddr --informative-errors --verbose`

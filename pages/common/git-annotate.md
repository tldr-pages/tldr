# git annotate

> Show commit hash and last author on each line of a file.
> Note: Use `git blame`.
> This only difference between `git annotate` and `git blame` is that the former has a slightly different output format, and is used only for backwards-compatibility, and provide a more familiar command name for people coming from other SCM systems.
> More information: <https://git-scm.com/docs/git-annotate>.

- Print file with author name and commit hash on each line:

`git annotate {{file}}`

- Print file with author email and commit hash on each line:

`git annotate -e {{file}}`

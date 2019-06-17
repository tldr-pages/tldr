# git check-ignore

> Analyse and debug Git ignore / exclude (".gitignore") files.
> More information: <https://git-scm.com/docs/git-check-ignore>.

- Check whether one or more space-separated files or directories are ignored:

`git check-ignore {{path/to/files_or_directories}}`

- Use pathnames, one per line, from stdin:

`git check-ignore --stdin < {{path/to/file_list}}`

- Do not check the index (used to debug why paths were tracked and not ignored):

`git check-ignore --no-index {{path/to/files_or_directories}}`

- Include details about the matching pattern for each path:

`git check-ignore --verbose {{path/to/files_or_directories}}`

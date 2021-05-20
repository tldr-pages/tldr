# git effort

> Display how much activity a file has had, showing commits per file and "active days" i.e. total number of days that contributed to the file.
> Part of `git-extras`.
> More information: <https://github.com/tj/git-extras/blob/master/Commands.md#git-effort>.

- Display each file, showing commits and active days:

`git effort`

- Display files receiving over a specific number of commits, showing commits and active days:

`git effort --above {{5}}`

- Display files committed to, from a specific author, showing commits and active days:

`git effort -- --author"{{username}}"`

- Display files committed to, from a specific time/date, showing commits and active days:

`git effort -- --since='{{last month}}'`

- Display files committed to, from specific chosen files, showing commits and active days:

`git effort {{path/to/file_or_directory}}`

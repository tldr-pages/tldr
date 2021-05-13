# git authors

> Display log or list of committers of a Git repository. Everything except `--list` will create a new file called `AUTHORS`.
> Part of `git-extras`.
> More information: <https://github.com/tj/git-extras/blob/master/Commands.md#git-authors>.

- Display a log of committers in the default editor, reading from the `AUTHORS` file:

`git authors`

- Print a full list of committers:

`git authors --list`

- Display a log of committers, excluding emails, in the default editor, reading from the `AUTHORS` file:

`git authors --no-email`

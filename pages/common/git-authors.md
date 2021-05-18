# git authors

> Display a list of committers of a Git repository. Everything except `--list` will append the list of commiters to the `AUTHORS` file.
> Part of `git-extras`.
> More information: <https://github.com/tj/git-extras/blob/master/Commands.md#git-authors>.

- Append the list of committers to the the `AUTHORS` file and open it in the default editor:

`git authors`

- Print a full list of committers:

`git authors --list`

- Append the list of committers, excluding emails, to the the `AUTHORS` file and open it in the default editor:

`git authors --no-email`

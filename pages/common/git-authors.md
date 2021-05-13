# git authors

> Display log or list of committers of a Git repository. If you aren't using the list command, a new file called AUTHORS will be created. Sorted by amount of commits.
> Part of `git-extras`.
> More information: <https://github.com/tj/git-extras/blob/master/Commands.md#git-authors>.

- Display a log of committers in the default editor, reading from the `AUTHORS` file:

`git authors`

- Print a full list of committers:

`git authors --list`

- Display full log of committers of the current Git repository, excluding emails, reading from the AUTHORS file, opened in your default editor:

`git authors --no-email`

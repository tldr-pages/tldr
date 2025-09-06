# git authors

> Generate a list of committers of a Git repository.
> Part of `git-extras`.
> More information: <https://manned.org/git-authors>.

- Print a full list of committers to `stdout` instead of to the `AUTHORS` file:

`git authors {{[-l|--list]}}`

- Append the list of committers to the `AUTHORS` file and open it in the default editor:

`git authors`

- Append the list of committers, excluding emails, to the `AUTHORS` file and open it in the default editor:

`git authors --no-email`

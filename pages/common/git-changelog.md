# git changelog

> Generate a changelog report from repository commits and tags.
> Part of `git-extras`.
> More information: <https://github.com/tj/git-extras/blob/master/Commands.md#git-changelog>.

- Update existing file or create a new `History.md` file with the commit messages since the latest Git tag:

`git changelog`

- List commits from the current version:

`git changelog --list`

- List a range of commits from the tag named `2.1.0` to now:

`git changelog --list --start-tag {{2.1.0}}`

- List pretty formatted range of commits between the tag `0.5.0` and the tag `1.0.0`:

`git changelog --start-tag {{0.5.0}} --final-tag {{1.0.0}}`

- List pretty formatted range of commits between the commit `0b97430` and the tag `1.0.0`:

`git changelog --start-commit {{0b97430}} --final-tag {{1.0.0}}`

- Specify `CHANGELOG.md` as the output file:

`git changelog {{CHANGELOG.md}}`

- Replace contents of current changelog file entirely:

`git changelog --prune-old`

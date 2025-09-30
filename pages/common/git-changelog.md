# git changelog

> Generate a changelog report from repository commits and tags.
> Part of `git-extras`.
> More information: <https://manned.org/git-changelog>.

- Update existing file or create a new `History.md` file with the commit messages since the latest Git tag:

`git changelog`

- List commits from the current version:

`git changelog {{[-l|--list]}}`

- List a range of commits from the tag named `2.1.0` to now:

`git changelog {{[-l|--list]}} {{[-s|--start-tag]}} {{2.1.0}}`

- List pretty formatted range of commits between the tag `0.5.0` and the tag `1.0.0`:

`git changelog {{[-s|--start-tag]}} {{0.5.0}} {{[-f|--final-tag]}} {{1.0.0}}`

- List pretty formatted range of commits between the commit `0b97430` and the tag `1.0.0`:

`git changelog --start-commit {{0b97430}} {{[-f|--final-tag]}} {{1.0.0}}`

- Specify `CHANGELOG.md` as the output file:

`git changelog {{CHANGELOG.md}}`

- Replace contents of current changelog file entirely:

`git changelog {{[-p|--prune-old]}}`

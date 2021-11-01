# git changelog

> Generate a changelog report from repository commits and tags.
> Part of `git-extras`.
> More information: <https://github.com/tj/git-extras/blob/master/Commands.md#git-changelog>.

- Updating existing file or creating a new History.md file with pretty formatted output:

`git changelog`

- Listing commits from the current version:

`git changelog --list`

- Listing a range of commits from 2.1.0 to now:

`git changelog --list --start-tag 2.1.0`

- Listing a pretty formatted range of commits between 0.5.0 and 1.0.0:

`git changelog --start-tag 0.5.0 --final-tag 1.0.0`

- Listing a pretty formatted range of commits between 0b97430 and 1.0.0:

`git changelog --start-commit 0b97430 --final-tag 1.0.0`

- Specifying a file for output:

`git changelog CHANGELOG.md`

- Replace contents of current changelog file entirely:

`git changelog --prune-old`

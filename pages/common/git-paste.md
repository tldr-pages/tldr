# git paste

> Send commits to a pastebin site using `pastebinit`.
> Part of `git-extras`.
> More information: <https://github.com/tj/git-extras/blob/master/Commands.md#git-paste>.

- Send commits to a pastebin site using `pastebinit`:

`git paste {{paste_url}}`

- Pass options understood by `git-rev-parse(1)` in order to select a different set of commits:

`git paste @^ {{paste_url}}`

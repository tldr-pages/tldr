# git paste

> Send commits to a pastebin site using `pastebinit`.
> Part of `git-extras`.
> More information: <https://github.com/tj/git-extras/blob/master/Commands.md#git-paste>.

- Send commits to a pastebin site using `pastebinit`:

`git paste {{paste_url}}`

- Pass options to `git format-patch` in order to select a different set of commits (`@^` selects the parent of HEAD, and so the currently checked out commit is sent):

`git paste {{@^}}`

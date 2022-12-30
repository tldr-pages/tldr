# git standup

> See commits from a specified user.
> Part of `git-extras`.
> More information: <https://github.com/tj/git-extras/blob/master/Commands.md#git-standup>.

- Show a given author's commits from the last 10 days:

`git standup -a {{name|email}} -d {{10}}`

- Show a given author's commits from the last 10 days and whether they are GPG signed:

`git standup -a {[name|email}} -d {{10}} -g`

- Show all the commits from all contributors for the last 10 days:

`git standup -a all -d {{10}}`

- Display help:

`git standup -h`

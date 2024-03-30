# git guilt

> Show total blame count for files with unstaged changes or calculate the change in blame between two revisions.
> Part of `git-extras`.
> More information: <https://github.com/tj/git-extras/blob/master/Commands.md#git-guilt>.

- Show total blame count:

`git guilt`

- Calculate the change in blame between two revisions:

`git guilt {{first_revision}} {{last_revision}}`

- Show author emails instead of names:

`git guilt --email`

- Ignore whitespace only changes when attributing blame:

`git guilt --ignore-whitespace`

- Find blame delta over the last three weeks:

`git guilt 'git log --until="3 weeks ago" --format="%H" -n 1'`

- Find blame delta over the last three weeks (git 1.8.5+):

`git guilt @{3.weeks.ago}`

# git guilt

> Show total blame count for files with unstaged changes or calculate the change in blame between two revisions.
> Part of `git-extras`.
> More information: <https://manned.org/git-guilt>.

- Show total blame count:

`git guilt`

- Calculate the change in blame between two revisions:

`git guilt {{first_revision}} {{last_revision}}`

- Show author emails instead of names:

`git guilt {{[-e|--email]}}`

- Ignore whitespace only changes when attributing blame:

`git guilt {{[-w|--ignore-whitespace]}}`

- Find blame delta over the last three weeks:

`git guilt 'git log --until "3 weeks ago" --format "%H" {{[-n|--max-count]}} 1'`

- Find blame delta over the last three weeks (git 1.8.5+):

`git guilt @{3.weeks.ago}`

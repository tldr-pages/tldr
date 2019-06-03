# git log

> Show a history of commits.
> More information: <https://git-scm.com/docs/git-log>.

- Show the sequence of commits starting from the current one, in reverse chronological order:

`git log`

- Show the history of a particular file or directory, including differences:

`git log -p {{path/to/file_or_directory}}`

- Show only the first line of each commit message:

`git log --oneline`

- Show an overview of which file(s) changed in each commit:

`git log --stat`

- Show a graph of commits in the current branch:

`git log --graph`

- Show a graph of all commits, tags and branches in the entire repo:

`git log --oneline --decorate --all --graph`

- Show only commits whose messages include a given string (case-insensitively):

`git log -i --grep {{search_string}}`

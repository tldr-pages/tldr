# git log

> Show a history of commits.

- Show the sequence of commits starting from the current one, in reverse chronological order:

`git log`

- Show the history of a particular file or directory, including differences:

`git log -p {{path}}`

- Show only the first line of each commit message:

`git log --oneline`

- Show all commits, tags and branches for the entire repo in a graph format:

`git log --oneline --decorate --all --graph`

- Show only commits whose messages include a given string (case-insensitively):

`git log -i --grep {{search_string}}`

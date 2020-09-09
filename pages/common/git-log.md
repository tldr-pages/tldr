# git log

> Show a history of commits.
> More information: <https://git-scm.com/docs/git-log>.

- Show the sequence of commits starting from the current one, in reverse chronological order of the git repository in the current working directory:

`git log`

- Show the history of a particular file or directory, including differences:

`git log -p {{path/to/file_or_directory}}`

- Show an overview of which file(s) changed in each commit:

`git log --stat`

- Show a graph of commits in the current branch using only the first line of each commit message:

`git log --oneline --graph`

- Show a graph of all commits, tags and branches in the entire repo:

`git log --oneline --decorate --all --graph`

- Show only commits whose messages include a given string (case-insensitively):

`git log -i --grep {{search_string}}`

- Show the last N commits from a certain author:

`git log -n {{number}} --author={{author}}`

- Show commits between two dates:

`git log --before={{date}} --after={{date}}`

# git-grep

> Find strings inside files as they existed anywhere in repo history. Accepts a lot of the same flags as regular grep. Learn more here: https://git-scm.com/docs/git-grep.

- Search for a string in working directory:

`git grep {{search_string}}`

- Search for string in files matching a pattern in working directory:

`git grep {{search_string}} -- {{file_glob_pattern}}`

- Search for a string in working directory, including submodules:

`git grep --recurse-submodules {{search_string}}`

- Search for a string in another point in history:

`git grep {{search_string}} HEAD~2`

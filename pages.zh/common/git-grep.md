# git-grep

> 在仓库的历史中查找文件内的字符串。
> 接受与常规 `grep` 相同的许多标志。
> 更多信息：<https://git-scm.com/docs/git-grep>。

- 在跟踪的文件中搜索字符串：

`git grep {{search_string}}`

- 在跟踪的文件中搜索匹配模式的文件中的字符串：

`git grep {{search_string}} -- {{file_glob_pattern}}`

- 在跟踪的文件中搜索字符串，包括子模块：

`git grep --recurse-submodules {{search_string}}`

- 在历史的特定点搜索字符串：

`git grep {{search_string}} {{HEAD~2}}`

- 在所有分支中搜索字符串：

`git grep {{search_string}} $(git rev-list --all)`
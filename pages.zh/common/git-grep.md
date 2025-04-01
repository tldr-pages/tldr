# git-grep

> 在仓库的历史记录中搜索字符串。
> 接受与常规 `grep` 类似的许多标志。
> 更多信息：<https://git-scm.com/docs/git-grep>。

- 在受跟踪的文件中搜索字符串：

`git grep {{search_string}}`

- 在受跟踪的文件中，搜索匹配模式的文件中的字符串：

`git grep {{search_string}} -- {{file_glob_pattern}}`

- 在受跟踪的文件中搜索字符串，包括子模块：

`git grep --recurse-submodules {{search_string}}`

- 在特定历史点搜索字符串：

`git grep {{search_string}} {{HEAD~2}}`

- 在所有分支中搜索字符串：

`git grep {{search_string}} $(git rev-list --all)`

# ned

> 类似于 `grep` 但具有强大的替换功能。
> 与 `sed` 不同，因为它不局限于行编辑。
> 更多信息： <https://github.com/nevdelap/ned>。

- 从当前目录递归搜索，忽略大小写：

`ned --ignore-case --recursive '{{^[dl]og}}' {{.}}`

- 搜索时始终显示彩色输出：

`ned --colors '{{^[dl]og}}' {{.}}`

- 搜索时从不显示彩色输出：

`ned --colors=never '{{^[dl]og}}' {{.}}`

- 搜索时忽略某些文件：

`ned --recursive --exclude '{{*.htm}}' '{{^[dl]og}}' {{.}}`

- 简单替换：

`ned '{{dog}}' --replace '{{cat}}' {{.}}`

- 使用编号组引用进行替换：

`ned '{{the ([a-z]+) dog and the ([a-z]+) dog}}' --replace '{{the $2 dog and the $1 dog}}' {{.}}`

- 替换时改变大小写：

`ned '{{([a-z]+) dog}}' --case-replacements --replace '{{\U$1\E! dog}}' --stdout {{.}}`

- 预览查找和替换的结果而不更新目标文件：

`ned '{{^[sb]ad}}' --replace '{{happy}}' --stdout {{.}}`
# git effort

> 显示文件的活动程度，包括每个文件的提交次数和“活跃天数”，即对文件有贡献的总天数。
> 属于 `git-extras`。
> 更多信息：<https://github.com/tj/git-extras/blob/master/Commands.md#git-effort>。

- 显示仓库中每个文件的提交次数和活跃天数：

`git effort`

- 显示被特定次数或更多次提交修改的文件，包括提交次数和活跃天数：

`git effort --above {{5}}`

- 显示被特定作者修改的文件，包括提交次数和活跃天数：

`git effort -- --author="{{username}}"`

- 显示自特定时间或日期以来被修改的文件，包括提交次数和活跃天数：

`git effort -- --since="{{last month}}"`

- 仅显示指定的文件或目录，包括提交次数和活跃天数：

`git effort {{path/to/file_or_directory1 path/to/file_or_directory2 ...}}`

- 显示特定目录中所有文件的提交次数和活跃天数：

`git effort {{path/to/directory/*}}`
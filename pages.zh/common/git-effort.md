# git effort

> 显示一个文件的活动量，展示每个文件的提交次数和“活跃天数”，即为文件贡献的总天数。
> 这是 `git-extras` 的一部分。
> 更多信息请访问: <https://github.com/tj/git-extras/blob/master/Commands.md#git-effort>。

- 显示仓库中的每个文件，展示提交次数和活跃天数：

`git effort`

- 显示被特定数量或更多提交修改的文件，展示提交次数和活跃天数：

`git effort --above {{5}}`

- 显示由特定作者修改的文件，展示提交次数和活跃天数：

`git effort -- --author="{{username}}"`

- 显示自特定时间/日期以来修改的文件，展示提交次数和活跃天数：

`git effort -- --since="{{last month}}"`

- 仅显示指定的文件或目录，展示提交次数和活跃天数：

`git effort {{path/to/file_or_directory1 path/to/file_or_directory2 ...}}`

- 显示特定目录中的所有文件，展示提交次数和活跃天数：

`git effort {{path/to/directory/*}}`
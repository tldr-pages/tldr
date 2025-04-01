# git add

> 将更改的文件添加到索引（暂存区）。
> 更多信息：<https://git-scm.com/docs/git-add>.

- 添加单个文件到索引：

`git add {{路径/到/文件}}`

- 添加所有文件（包括已跟踪的和未跟踪的）:

`git add {{[-A|--all]}}`

- 从当前文件夹开始递归地添加所有文件：

`git add .`

- 只添加已跟踪的文件：

`git add {{[-u|--update]}}`

- 忽略的文件也添加：

`git add {{[-f|--force]}}`

- 交互式挑选部分修改并暂存：

`git add {{[-p|--patch]}}`

- 交互式挑选指定文件的部分修改并暂存：

`git add {{[-p|--patch]}} {{路径/到/文件}}`

- 在交互模式下暂存文件：

`git add {{[-i|--interactive]}}`

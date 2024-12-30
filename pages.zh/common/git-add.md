# git add

> 将更改的文件添加到索引中。
> 更多信息：<https://git-scm.com/docs/git-add>。

- 将文件添加到索引：

`git add {{path/to/file}}`

- 添加所有文件（已跟踪和未跟踪的）：

`git add {{-A|--all}}`

- 添加当前文件夹中的所有文件：

`git add .`

- 仅添加已经跟踪的文件：

`git add {{-u|--update}}`

- 同时添加被忽略的文件：

`git add {{-f|--force}}`

- 交互式地暂存文件的部分内容：

`git add {{-p|--patch}}`

- 交互式地暂存指定文件的部分内容：

`git add {{-p|--patch}} {{path/to/file}}`

- 交互式地暂存文件：

`git add {{-i|--interactive}}`
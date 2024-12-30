# cvs

> 并发版本系统，一种版本控制系统。
> 更多信息：<https://cvs.nongnu.org>。

- 创建一个新的代码库（需要将 `CVSROOT` 环境变量在外部设置）：

`cvs -d {{path/to/repository}} init`

- 将项目添加到代码库中：

`cvs import -m "{{message}}" {{project_name}} {{version}} {{vendor}}`

- 检出一个项目：

`cvs checkout {{project_name}}`

- 显示对文件所做的更改：

`cvs diff {{path/to/file}}`

- 添加一个文件：

`cvs add {{path/to/file}}`

- 提交一个文件：

`cvs commit -m "{{message}}" {{path/to/file}}`

- 从远程代码库更新工作目录：

`cvs update`
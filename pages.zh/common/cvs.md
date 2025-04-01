# cvs

> 并发版本系统，一个版本控制系统。
> 更多信息：<https://manned.org/cvs>。

- 创建一个新的仓库（需要外部设置 `CVSROOT` 环境变量）：

`cvs -d {{path/to/repository}} init`

- 将项目添加到仓库中：

`cvs import -m "{{message}}" {{project_name}} {{version}} {{vendor}}`

- 检出一个项目：

`cvs checkout {{project_name}}`

- 显示文件的更改：

`cvs diff {{path/to/file}}`

- 添加文件：

`cvs add {{path/to/file}}`

- 提交文件：

`cvs commit -m "{{message}}" {{path/to/file}}`

- 从远程仓库更新工作目录：

`cvs update`
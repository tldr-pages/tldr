# git magic

> 自动执行添加、提交和推送操作。
> `git-extras` 的一部分。
> 更多信息：<https://manned.org/git-magic>.

- 使用生成的提交信息提交更改：

`git magic`

- [a]dd 未跟踪的文件并使用生成的提交信息提交更改：

`git magic -a`

- 使用自定义的 [m]essage 提交更改：

`git magic -m "{{custom_commit_message}}"`

- 在提交前 [e]dit 提交 [m]essage：

`git magic -em "{{custom_commit_message}}"`

- 提交更改并 [p]ush 到远程仓库：

`git magic -p`

- 使用 [f]orce [p]ush 强制推送提交的更改：

`git magic -fp`
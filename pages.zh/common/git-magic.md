# git 魔法

> 自动化添加、提交和推送流程。
> 作为 `git-extras` 的一部分。
> 更多信息：<https://github.com/tj/git-extras/blob/master/Commands.md#git-magic>。

- 使用生成的消息提交更改：

`git magic`

- [a] 添加未跟踪的文件并使用生成的消息提交更改：

`git magic -a`

- 使用自定义 [m] 消息提交更改：

`git magic -m "{{custom_commit_message}}"`

- 在提交之前 [e] 编辑提交 [m] 消息：

`git magic -em "{{custom_commit_message}}"`

- 提交更改并 [p] 推送到远程：

`git magic -p`

- 使用 [f] 强制 [p] 推送到远程提交更改：

`git magic -fp`
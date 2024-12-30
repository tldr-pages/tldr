# git standup

> 查看指定用户的提交记录。
> 该命令是 `git-extras` 的一部分。
> 更多信息：<https://github.com/tj/git-extras/blob/master/Commands.md#git-standup>。

- 显示给定作者在过去10天的提交记录：

`git standup -a {{name|email}} -d {{10}}`

- 显示给定作者在过去10天的提交记录及其是否经过GPG签名：

`git standup -a {{name|email}} -d {{10}} -g`

- 显示所有贡献者在过去10天的所有提交记录：

`git standup -a all -d {{10}}`

- 显示帮助信息：

`git standup -h`
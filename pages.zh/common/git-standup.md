# git standup

> 查看指定用户的提交记录。
> 属于 `git-extras` 的一部分。
> 更多信息：<https://github.com/tj/git-extras/blob/master/Commands.md#git-standup>.

- 显示指定作者在最近10天内的提交记录：

`git standup -a {{name|email}} -d {{10}}`

- 显示指定作者在最近10天内的提交记录，并显示这些提交是否使用了GPG签名：

`git standup -a {{name|email}} -d {{10}} -g`

- 显示所有贡献者在最近10天内的所有提交记录：

`git standup -a all -d {{10}}`

- 显示帮助信息：

`git standup -h`

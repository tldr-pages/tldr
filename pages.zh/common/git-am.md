# git am

> 应用补丁文件并创建提交。当通过电子邮件接收提交时非常有用。
> 另见 `git format-patch`，它可以生成补丁文件。
> 更多信息：<https://git-scm.com/docs/git-am>。

- 根据本地补丁文件应用并提交更改：

`git am {{path/to/file.patch}}`

- 根据远程补丁文件应用并提交更改：

`curl -L {{https://example.com/file.patch}} | git apply`

- 中止应用补丁文件的过程：

`git am --abort`

- 尽可能应用补丁文件的内容，将失败的块保存到拒绝文件中：

`git am --reject {{path/to/file.patch}}`
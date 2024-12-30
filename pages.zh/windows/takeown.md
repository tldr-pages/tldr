# takeown

> 获取文件或目录的所有权。
> 更多信息：<https://learn.microsoft.com/windows-server/administration/windows-commands/takeown>。

- 获取指定文件的所有权：

`takeown /f {{path\to\file}}`

- 获取指定目录的所有权：

`takeown /d {{path\to\directory}}`

- 获取指定目录及所有子目录的所有权：

`takeown /r /d {{path\to\directory}}`

- 将所有权更改为管理员组，而不是当前用户：

`takeown /a /f {{path\to\file}}`
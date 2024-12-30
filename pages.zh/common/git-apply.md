# git apply

> 将补丁应用于文件和/或索引，而不创建提交。
> 另请参见 `git am`，它应用补丁并创建提交。
> 更多信息：<https://git-scm.com/docs/git-apply>。

- 打印关于补丁文件的消息：

`git apply --verbose {{path/to/file}}`

- 应用补丁并将补丁文件添加到索引：

`git apply --index {{path/to/file}}`

- 应用远程补丁文件：

`curl -L {{https://example.com/file.patch}} | git apply`

- 输出输入的 diffstat 并应用补丁：

`git apply --stat --apply {{path/to/file}}`

- 以相反的方式应用补丁：

`git apply --reverse {{path/to/file}}`

- 将补丁结果存储在索引中而不修改工作树：

`git apply --cache {{path/to/file}}`
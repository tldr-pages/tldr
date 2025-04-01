# git apply

> 将补丁应用到文件和/或索引，但不创建提交。
> 参见 `git am`，它在应用补丁的同时也会创建提交。
> 更多信息：<https://git-scm.com/docs/git-apply>。

- 打印关于已修补文件的消息：

`git apply --verbose {{path/to/file}}`

- 应用并添加已修补的文件到索引：

`git apply --index {{path/to/file}}`

- 应用远程补丁文件：

`curl -L {{https://example.com/file.patch}} | git apply`

- 输出输入的差异统计信息并应用补丁：

`git apply --stat --apply {{path/to/file}}`

- 反向应用补丁：

`git apply --reverse {{path/to/file}}`

- 将补丁结果存储在索引中，不修改工作树：

`git apply --cache {{path/to/file}}`
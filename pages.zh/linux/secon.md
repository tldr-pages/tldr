# secon

> 获取文件、进程ID、当前执行上下文或上下文规范的 SELinux 安全上下文。
> 参见：`semanage`, `runcon`, `chcon`。
> 更多信息：<https://manned.org/secon>。

- 获取当前执行上下文的安全上下文：

`secon`

- 获取进程的当前安全上下文：

`secon --pid {{1}}`

- 获取文件的当前安全上下文，解析所有中间符号链接：

`secon --file {{path/to/file_or_directory}}`

- 获取符号链接本身的当前安全上下文（不解析）：

`secon --link {{path/to/symlink}}`

- 解析并解释上下文规范：

`secon {{system_u:system_r:container_t:s0:c899,c900}}`

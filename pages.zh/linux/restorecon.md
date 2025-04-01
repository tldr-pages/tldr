# restorecon

> 根据持久规则恢复文件或目录上的 SELinux 安全上下文。
> 参见：`semanage-fcontext`。
> 更多信息：<https://manned.org/restorecon>。

- 查看文件或目录的当前安全上下文：

`ls -dlZ {{path/to/file_or_directory}}`

- 恢复文件或目录的安全上下文：

`restorecon {{path/to/file_or_directory}}`

- 递归恢复目录的安全上下文，并显示所有更改的标签：

`restorecon -R -v {{path/to/directory}}`

- 递归恢复目录的安全上下文，使用所有可用线程，并显示进度：

`restorecon -R -T {{0}} -p {{path/to/directory}}`

- 预览将要进行的标签更改，但不实际应用：

`restorecon -R -n -v {{path/to/directory}}`
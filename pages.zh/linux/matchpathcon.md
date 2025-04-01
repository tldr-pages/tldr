# matchpathcon

> 查询路径的持久 SELinux 安全上下文设置。
> 参见：`semanage-fcontext`, `secon`, `chcon`, `restorecon`。
> 更多信息：<https://manned.org/matchpathcon.8>。

- 查询绝对路径的持久安全上下文设置：

`matchpathcon {{/path/to/file}}`

- 限制查询到特定文件类型的设置：

`matchpathcon -m {{file|dir|pipe|chr_file|blk_file|lnk_file|sock_file}} {{/path/to/file}}`

- [V]erify 验证路径的持久安全上下文与当前安全上下文是否一致：

`matchpathcon -V {{/path/to/file}}`

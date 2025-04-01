# semanage permissive

> 管理持久的 SELinux 宽容域。
> 请注意，这实际上使进程不受限制。对于长期使用，建议正确配置 SELinux。
> 参见：`semanage`，`getenforce`，`setenforce`。
> 更多信息：<https://manned.org/semanage-permissive>。

- 列出所有处于宽容模式的进程类型（也称为域）：

`sudo semanage permissive {{[-l|--list]}}`

- 为域设置宽容模式：

`sudo semanage permissive {{[-a|--add]}} {{httpd_t}}`

- 取消域的宽容模式：

`sudo semanage permissive {{[-d|--delete]}} {{httpd_t}}`
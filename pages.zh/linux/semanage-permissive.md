# semanage permissive

> 管理持久的 SELinux 宽松域。
> 请注意，这实际上使得该进程处于未受限制的状态。对于长期使用，建议正确配置 SELinux。
> 另请参见：`semanage`，`getenforce`，`setenforce`。
> 更多信息：<https://manned.org/semanage-permissive>。

- 列出所有处于宽松模式的进程类型（即域）：

`sudo semanage permissive {{-l|--list}}`

- 设置或取消某个域的宽松模式：

`sudo semanage permissive {{-a|--add|-d|--delete}} {{httpd_t}}`
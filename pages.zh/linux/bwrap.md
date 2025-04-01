# bwrap

> 在轻量级沙箱中运行程序。
> 更多信息：<https://manned.org/bwrap>。

- 在只读环境中运行程序：

`bwrap --ro-bind / / {{/bin/bash}}`

- 为环境提供设备访问、进程信息，并为其创建 `tmpfs`：

`bwrap --dev-bind /dev /dev --proc /proc --ro-bind / / --tmpfs /tmp {{/bin/bash}}`

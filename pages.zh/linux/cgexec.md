# cgexec

> 限制、测量和控制进程使用的资源。
> 存在多种 cgroup 类型（又称控制器），例如 `cpu`、`memory` 等。
> 更多信息：<https://manned.org/cgexec>。

- 在给定的 cgroup 中使用给定控制器执行进程：

`cgexec -g {{controller}}:{{cgroup_name}} {{process_name}}`
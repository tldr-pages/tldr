# cgexec

> 限制、测量和控制进程使用的资源。
> 多种 cgroup 类型（控制器）存在，例如 `cpu`、`memory` 等。
> 更多信息：<https://manned.org/cgexec>.

- 在指定的 cgroup 和控制器中执行进程：

`cgexec -g {{controller}}:{{cgroup_name}} {{process_name}}`

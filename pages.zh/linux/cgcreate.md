# cgcreate

> 创建控制组（cgroups），用于限制、测量和控制进程使用的资源。
> `cgroups` 类型可以是 `memory`、`cpu`、`net_cls` 等。
> 更多信息：<https://manned.org/cgcreate>.

- 创建一个新的组：

`cgcreate -g {{group_type}}:{{group_name}}`

- 创建具有多个 `cgroup` 类型的新组：

`cgcreate -g {{group_type1}},{{group_type2}}:{{group_name}}`

- 创建一个子组：

`mkdir /sys/fs/cgroup/{{group_type}}/{{group_name}}/{{subgroup_name}}`

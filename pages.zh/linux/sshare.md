# sshare

> 列出与集群关联的共享信息。
> 更多信息：<https://slurm.schedmd.com/sshare.html>。

- 列出 Slurm 共享信息：

`sshare`

- 控制输出格式：

`sshare --{{parsable|parsable2|json|yaml}}`

- 控制要显示的字段：

`sshare --format={{format_string}}`

- 仅显示指定用户的共享信息：

`sshare --users={{user_id_1,user_id_2,...}}`

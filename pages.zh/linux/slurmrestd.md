# slurmrestd

> 通过 REST API 访问 Slurm 的接口。可以以两种模式使用：*Inetd 模式* 和 *监听模式*。
> 更多信息：<https://slurm.schedmd.com/slurmrestd.html>.

- 在处理客户端请求之前更改组 ID（并删除辅助组）：

`slurmrestd --g {{group_id}} {{[host]:port | unix:/path/to/socket}}`

- 以逗号分隔的要加载的身份验证插件列表：

`slurmrestd -a {{authentication_plugins}} {{[host]:port | unix:/path/to/socket}}`

- 从指定文件读取 Slurm 配置：

`slurmrestd -f {{path/to/file}}`

- 在处理客户端请求之前更改用户 ID：

`slurmrestd -u {{user_id}}`

- 显示帮助信息：

`slurmrestd -h`

- 显示版本信息：

`slurmrestd -V`
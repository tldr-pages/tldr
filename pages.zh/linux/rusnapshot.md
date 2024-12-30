# rusnapshot

> 用Rust编写的BTRFS快照工具。
> 更多信息：<https://github.com/Edu4rdSHL/rusnapshot>。

- 使用配置文件创建快照：

`sudo rusnapshot --config {{path/to/config.toml}} --cr`

- 列出已创建的快照：

`sudo rusnapshot -c {{path/to/config.toml}} --list`

- 通过ID或快照名称删除快照：

`sudo rusnapshot -c {{path/to/config.toml}} --del --id {{snapshot_id}}`

- 删除所有`hourly`快照：

`sudo rusnapshot -c {{path/to/config.toml}} --list --keep {{0}} --clean --kind {{hourly}}`

- 创建一个可读写的快照：

`sudo rusnapshot -c {{path/to/config.toml}} --cr --rw`

- 恢复快照：

`sudo rusnapshot -c {{path/to/config.toml}} --id {{snapshot_id}} --restore`
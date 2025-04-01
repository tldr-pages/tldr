# rustic

> 使用 Rust 创建快速、加密、去重的备份。
> 更多信息：<https://github.com/rustic-rs/rustic>.

- 初始化一个新的仓库：

`rustic init --repository {{/srv/rustic-repo}}`

- 创建一个文件或目录的备份到仓库：

`rustic backup --repository {{/srv/rustic-repo}} {{path/to/file_or_directory}}`
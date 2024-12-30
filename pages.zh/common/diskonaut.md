# diskonaut

> 终端磁盘空间导航器，使用 Rust 编写。
> 更多信息：<https://github.com/imsnif/diskonaut>。

- 在当前目录中启动 `diskonaut`：

`diskonaut`

- 在特定目录中启动 `diskonaut`：

`diskonaut {{path/to/directory}}`

- 显示文件大小而不是它们在磁盘上的块使用情况：

`diskonaut --apparent-size {{path/to/directory}}`

- 禁用删除确认：

`diskonaut --disable-delete-confirmation`
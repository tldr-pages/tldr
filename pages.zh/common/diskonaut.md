# diskonaut

> 终端磁盘空间导航器，使用 Rust 编写。
> 更多信息：<https://github.com/imsnif/diskonaut>.

- 在当前目录中启动 `diskonaut`：

`diskonaut`

- 在指定目录中启动 `diskonaut`：

`diskonaut {{path/to/directory}}`

- 显示文件的实际大小而非磁盘上的块占用：

`diskonaut --apparent-size {{path/to/directory}}`

- 禁用删除确认：

`diskonaut --disable-delete-confirmation`

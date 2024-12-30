# trashy

> 一个用 Rust 编写的 `rm` 和 `trash-cli` 的替代品。
> 更多信息请访问：<https://github.com/oberblastmeister/trashy>。

- 将特定文件移动到回收站：

`trash {{path/to/file}}`

- 将特定文件移动到回收站：

`trash {{path/to/file1 path/to/file2 ...}}`

- 列出回收站中的项目：

`trash list`

- 从回收站恢复特定文件：

`trash restore {{file}}`

- 从回收站中删除特定文件：

`trash empty {{file}}`

- 从回收站恢复所有文件：

`trash restore --all`

- 从回收站中删除所有文件：

`trash empty --all`
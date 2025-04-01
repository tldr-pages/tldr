# mg

> 基于 `emacs` 的小型、快速且可移植的文本编辑器。
> 更多信息：<https://github.com/hboetes/mg>.

- 打开文件进行编辑：

`mg {{path/to/file}}`

- 在指定行号处打开文件：

`mg +{{line_number}} {{path/to/file}}`

- 以只读模式打开文件：

`mg -R {{path/to/file1 path/to/file2 ...}}`

- 编辑时禁用 `~` 备份文件：

`mg -n {{path/to/file}}`
# Atom

> 一个跨平台的可插拔文本编辑器。
> 插件由 `apm` 管理。
> 注意：Atom 已停止更新，不再积极维护。
> 更多信息：<https://atom.io/>.

- 打开文件或目录：

`atom {{path/to/file_or_directory}}`

- 在 [n]ew 窗口中打开文件或目录：

`atom -n {{path/to/file_or_directory}}`

- 在现有窗口中打开文件或目录：

`atom --add {{path/to/file_or_directory}}`

- 以安全模式打开 Atom（不加载任何额外的包）：

`atom --safe`

- 防止 Atom 进入后台，使 Atom 保持连接到终端：

`atom --foreground`

- 等待 Atom 窗口关闭后再返回（对 Git 提交编辑器有用）：

`atom --wait`
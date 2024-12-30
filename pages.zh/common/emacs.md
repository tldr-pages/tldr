# emacs

> 可扩展、可定制、自我文档化的实时显示编辑器。
> 另见 `emacsclient`。
> 更多信息：<https://www.gnu.org/software/emacs>。

- 启动 Emacs 并打开一个文件：

`emacs {{path/to/file}}`

- 在指定行号打开一个文件：

`emacs +{{line_number}} {{path/to/file}}`

- 将一个 Emacs Lisp 文件作为脚本运行：

`emacs --script {{path/to/file.el}}`

- 以控制台模式启动 Emacs（不使用 X 窗口）：

`emacs --no-window-system`

- 在后台启动 Emacs 服务器（可通过 `emacsclient` 访问）：

`emacs --daemon`

- 停止正在运行的 Emacs 服务器及其所有实例，并在有未保存文件时请求确认：

`emacsclient --eval '(save-buffers-kill-emacs)'`

- 在 Emacs 中保存文件：

`<Ctrl> + X, <Ctrl> + S`

- 退出 Emacs：

`<Ctrl> + X, <Ctrl> + C`
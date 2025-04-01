# emacs

> 可扩展、可自定义、自文档化的实时显示编辑器。
> 请参见 `emacsclient`。
> 更多信息：<https://www.gnu.org/software/emacs>。

- 启动 Emacs 并打开一个文件：

`emacs {{path/to/file}}`

- 打开一个文件并定位到指定行号：

`emacs +{{line_number}} {{path/to/file}}`

- 作为脚本运行 Emacs Lisp 文件：

`emacs --script {{path/to/file.el}}`

- 以控制台模式启动 Emacs（不使用 X 窗口）：

`emacs {{[-nw|--no-window-system]}}`

- 在后台启动 Emacs 服务器（可通过 `emacsclient` 访问）：

`emacs --daemon`

- 停止正在运行的 Emacs 服务器及其所有实例，并在有未保存文件时询问确认：

`emacsclient --eval '(save-buffers-kill-emacs)'`

- 在 Emacs 中保存文件：

`<Ctrl x><Ctrl s>`

- 退出 Emacs：

`<Ctrl x><Ctrl c>`
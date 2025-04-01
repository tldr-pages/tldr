# emacsclient

> 在现有的 Emacs 服务器中打开文件。
> 另请参见 `emacs`。
> 更多信息：<https://www.gnu.org/software/emacs/manual/html_node/emacs/emacsclient-Options.html>。

- 在现有的 Emacs 服务器中打开文件（如果有可用的 GUI）：

`emacsclient {{path/to/file}}`

- 以控制台模式打开文件（不使用 X 窗口）：

`emacsclient {{[-nw|--no-window-system]}} {{path/to/file}}`

- 在新的 Emacs 窗口中打开文件：

`emacsclient {{[-c|--create-frame]}} {{path/to/file}}`

- 执行命令，将输出打印到 `stdout`，然后退出：

`emacsclient {{[-e|--eval]}} '({{command}})'`

- 指定一个备用编辑器，以防没有运行 Emacs 服务器：

`emacsclient {{[-a|--alternate-editor]}} {{editor}} {{path/to/file}}`

- 停止运行的 Emacs 服务器及其所有实例，并在未保存文件时请求确认：

`emacsclient {{[-e|--eval]}} '(save-buffers-kill-emacs)'`

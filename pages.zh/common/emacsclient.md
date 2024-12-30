# emacsclient

> 在现有的 Emacs 服务器中打开文件。
> 另见 `emacs`。
> 更多信息：<https://www.gnu.org/software/emacs/manual/html_node/emacs/emacsclient-Options.html>。

- 在现有的 Emacs 服务器中打开文件（如果可用则使用 GUI）：

`emacsclient {{path/to/file}}`

- 在控制台模式下打开文件（没有 X 窗口）：

`emacsclient --no-window-system {{path/to/file}}`

- 在新的 Emacs 窗口中打开文件：

`emacsclient --create-frame {{path/to/file}}`

- 评估一个命令，将输出打印到 `stdout`，然后退出：

`emacsclient --eval '({{command}})'`

- 指定一个备用编辑器，以防没有正在运行的 Emacs 服务器：

`emacsclient --alternate-editor {{editor}} {{path/to/file}}`

- 停止一个正在运行的 Emacs 服务器及其所有实例，并在有未保存文件时请求确认：

`emacsclient --eval '(save-buffers-kill-emacs)'`
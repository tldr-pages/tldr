# msgfmt

> 将消息目录编译为二进制格式。
> 更多信息：<https://www.gnu.org/software/gettext/manual/html_node/msgfmt-Invocation.html>.

- 将文件编译为 `messages.mo`：

`msgfmt {{file.po}}`

- 将 `.po` 文件转换为 `.mo` 文件：

`msgfmt {{path/to/file.po}} {{[-o|--output-file]}} {{path/to/file.mo}}`

- 显示帮助：

`msgfmt {{[-h|--help]}}`
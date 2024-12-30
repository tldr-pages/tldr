# cut

> 从 `stdin` 或文件中剪切字段。
> 更多信息：<https://www.gnu.org/software/coreutils/manual/html_node/cut-invocation.html>。

- 打印每行的特定 [c]haracter/[f]ield 范围：

`{{command}} | cut --{{characters|fields}} {{1|1,10|1-10|1|--10}}`

- 使用特定 [d]elimiter 打印每行的 [f]ield 范围：

`{{command}} | cut --delimiter "{{,}}" --fields {{1}}`

- 打印特定文件每行的 [c]haracter 范围：

`cut --characters {{1}} {{path/to/file}}`

- 打印以 `NUL` 结束的行的特定 [f]ields（例如，像 `find . -print0` 一样），而不是换行符：

`{{command}} | cut --zero-terminated --fields {{1}}`
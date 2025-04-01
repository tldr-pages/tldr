# groff

> GNU 替代 `troff` 和 `nroff` 排版工具。
> 更多信息：<https://www.gnu.org/software/groff/manual/groff.html.node/Groff-Options.html>。

- 为 PostScript 打印机格式化输出，并将输出保存到文件：

`groff {{path/to/input.roff}} > {{path/to/output.ps}}`

- 使用 ASCII 输出设备渲染 man 页面，并使用分页器显示：

`groff -man -T ascii {{path/to/manpage.1}} | less --RAW-CONTROL-CHARS`

- 将 man 页面渲染为 HTML 文件：

`groff -man -T html {{path/to/manpage.1}} > {{path/to/manpage.html}}`

- 使用 [me] 宏集格式化包含 [t] 表格和 [p] 图片的 roff 文件为 PDF，并保存输出：

`groff {{-t}} {{-p}} -{{me}} -T {{pdf}} {{path/to/input.me}} > {{path/to/output.pdf}}`

- 使用 `grog` 工具推断的预处理器和宏选项运行 `groff` 命令：

`eval "$(grog -T utf8 {{path/to/input.me}})"`
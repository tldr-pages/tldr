# groff

> GNU 替代 `troff` 和 `nroff` 排版工具。
> 更多信息请查看: <https://www.gnu.org/software/groff>。

- 为 PostScript 打印机格式化输出，并将输出保存到文件：

`groff {{path/to/input.roff}} > {{path/to/output.ps}}`

- 使用 ASCII 输出设备渲染手册页，并通过分页器显示：

`groff -man -T ascii {{path/to/manpage.1}} | less --RAW-CONTROL-CHARS`

- 将手册页渲染为 HTML 文件：

`groff -man -T html {{path/to/manpage.1}} > {{path/to/manpage.html}}`

- 使用 [me] 宏集将包含 [t] 表和 [p] 图片的 roff 文件排版为 PDF，并保存输出：

`groff {{-t}} {{-p}} -{{me}} -T {{pdf}} {{path/to/input.me}} > {{path/to/output.pdf}}`

- 运行带有预处理器和宏选项的 `groff` 命令，这些选项由 `grog` 工具猜测：

`eval "$(grog -T utf8 {{path/to/input.me}})"`
# inkmake

> 使用 Inkscape 后端的 GNU Makefile 风格 SVG 导出。
> 更多信息请访问: <https://github.com/wader/inkmake>。

- 导出指定 Inkfile 的 SVG 文件：

`inkmake {{path/to/Inkfile}}`

- 执行 Inkfile 并显示详细信息：

`inkmake --verbose {{path/to/Inkfile}}`

- 执行 Inkfile，指定 SVG 输入文件和输出文件：

`inkmake --svg {{path/to/file.svg}} --out {{path/to/output_image}} {{path/to/Inkfile}}`

- 使用自定义的 Inkscape 二进制文件作为后端：

`inkmake --inkscape {{/Applications/Inkscape.app/Contents/Resources/bin/inkscape}} {{path/to/Inkfile}}`

- 显示帮助信息：

`inkmake --help`
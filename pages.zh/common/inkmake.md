# inkmake

> 使用 Inkscape 后端以 GNU Makefile 风格导出 SVG。
> 更多信息：<https://github.com/wader/inkmake>.

- 执行指定的 Inkfile 导出 SVG 文件：

`inkmake {{path/to/Inkfile}}`

- 执行 Inkfile 并显示详细信息：

`inkmake --verbose {{path/to/Inkfile}}`

- 执行 Inkfile，指定 SVG 输入文件和输出文件：

`inkmake --svg {{path/to/file.svg}} --out {{path/to/output_image}} {{path/to/Inkfile}}`

- 使用自定义的 Inkscape 二进制文件作为后端：

`inkmake --inkscape {{/Applications/Inkscape.app/Contents/Resources/bin/inkscape}} {{path/to/Inkfile}}`

- 显示帮助：

`inkmake --help`

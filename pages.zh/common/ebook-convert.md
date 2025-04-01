# ebook-convert

> 可用于在常见格式之间转换电子书，例如 PDF、EPUB 和 MOBI。
> 是 Calibre 电子书库工具的一部分。
> 更多信息：<https://manual.calibre-ebook.com/generated/en/ebook-convert.html>.

- 将电子书转换为另一种格式：

`ebook-convert {{path/to/input_file}} {{output_file}}`

- 将 Markdown 或 HTML 转换为带有目录、标题和作者的电子书：

`ebook-convert {{path/to/input_file}} {{output_file}} --level1-toc="//h:h1" --level2-toc="//h:h2" --level3-toc="//h:h3" --title={{title}} --authors={{author}}`

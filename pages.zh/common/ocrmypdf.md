# ocrmypdf

> 从扫描的 PDF 或文本图像生成可搜索的 PDF 或 PDF/A。
> 更多信息：<https://ocrmypdf.readthedocs.io/en/latest/cookbook.html>。

- 从扫描的 PDF 或图像文件创建新的可搜索 PDF/A 文件：

`ocrmypdf {{path/to/input_file}} {{path/to/output.pdf}}`

- 用可搜索的 PDF 文件替换扫描的 PDF 文件：

`ocrmypdf {{path/to/file.pdf}} {{path/to/file.pdf}}`

- 跳过已经包含文本的混合格式输入 PDF 文件的页面：

`ocrmypdf --skip-text {{path/to/input.pdf}} {{path/to/output.pdf}}`

- 清理、校正倾斜和旋转低质量扫描的页面：

`ocrmypdf --clean --deskew --rotate-pages {{path/to/input_file}} {{path/to/output.pdf}}`

- 设置可搜索 PDF 文件的元数据：

`ocrmypdf --title "{{title}}" --author "{{author}}" --subject "{{subject}}" --keywords "{{keyword; key phrase; ...}}" {{path/to/input_file}} {{path/to/output.pdf}}`

- 显示帮助：

`ocrmypdf --help`

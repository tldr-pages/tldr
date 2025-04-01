# xmlto

> 应用 XSL 样式表到 XML 文档。
> 更多信息：<https://pagure.io/xmlto>.

- 将 DocBook XML 文档转换为 PDF 格式：

`xmlto {{pdf}} {{document.xml}}`

- 将 DocBook XML 文档转换为 HTML 格式，并将生成的文件存储在单独的目录中：

`xmlto -o {{path/to/html_files}} {{html}} {{document.xml}}`

- 将 DocBook XML 文档转换为单个 HTML 文件：

`xmlto {{html-nochunks}} {{document.xml}}`

- 在转换 DocBook XML 文档时指定要使用的样式表：

`xmlto -x {{stylesheet.xsl}} {{output_format}} {{document.xml}}`
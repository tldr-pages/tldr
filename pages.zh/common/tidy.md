# tidy

> 清理并美化 HTML、XHTML 和 XML 文件。
> 注意：`tidy` 无法保留原始的缩进。
> 更多信息：<https://api.html-tidy.org/tidy/tidylib_api_5.2.0/tidy_cmd.html>.

- 美化 HTML 文件：

`tidy {{path/to/file.html}}`

- 启用缩进，每行限制为 100 个字符，并保存到 `output.html`：

`tidy {{[-i|--indent]}} y {{[-w|--wrap]}} 100 {{[-o|-output]}} {{path/to/output.html}} {{path/to/file.html}}`

- 使用配置文件就地修改 HTML 文件：

`tidy -config {{path/to/configuration}} {{[-m|-modify]}} {{path/to/file.html}}`

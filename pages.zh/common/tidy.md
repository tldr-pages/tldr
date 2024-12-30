# tidy

> 清理和美化 HTML、XHTML 和 XML 文件。
> 注意：`tidy` 无法保留原始缩进。
> 更多信息：<https://api.html-tidy.org/tidy/tidylib_api_5.2.0/tidy_cmd.html>。

- 美化一个 HTML 文件：

`tidy {{path/to/file.html}}`

- 启用 [i]ndentation，设置每行最多 100 字符，保存为 `output.html`：

`tidy --indent y --wrap 100 -output {{path/to/output.html}} {{path/to/file.html}}`

- 使用配置文件在原位修改 HTML 文件：

`tidy -config {{path/to/configuration}} -modify {{path/to/file.html}}`
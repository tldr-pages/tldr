# olevba

> 解析 OLE 和 OpenXML 文件（例如 DOC、XLS、PPT 等），提取 VBA 宏，去混淆，并分析恶意代码。
> 是 `python-oletools` 套件的一部分。
> 更多信息：<https://github.com/decalage2/oletools>。

- 分析文件，显示宏代码和分析结果：

`olevba {{path/to/file}}`

- 递归分析目录中所有受支持的文件：

`olevba -r {{path/to/directory}}`

- 为加密的 Microsoft Office 文件提供密码（可以重复）：

`olevba --password {{password}} {{path/to/encrypted_file}}`

- 仅显示分析结果，不显示宏源代码：

`olevba -a {{path/to/file}}`

- 仅显示宏源代码：

`olevba -c {{path/to/file}}`

- 显示混淆字符串及其解码内容：

`olevba --decode {{path/to/file}}`
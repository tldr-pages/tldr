# vsce

> Visual Studio Code 的扩展管理工具。
> 更多信息：<https://github.com/microsoft/vscode-vsce>。

- 列出指定发行商创建的所有扩展：

`vsce list {{publisher}}`

- 发布扩展，指定主要、次要或补丁版本：

`vsce publish {{major|minor|patch}}`

- 取消发布扩展：

`vsce unpublish {{extension_id}}`

- 将当前工作目录打包为 `.vsix` 文件：

`vsce package`

- 显示扩展的元数据：

`vsce show {{extension_id}}`
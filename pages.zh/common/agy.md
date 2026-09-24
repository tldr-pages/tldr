# agy

> Google 的代理式开发平台。
> 更多信息：<https://antigravity.google/docs>。

- 打开特定文件或目录：

`agy {{路径/到/文件或目录}}`

- 比较两个文件：

`agy {{[-d|--diff]}} {{路径/到/文件1}} {{路径/到/文件2}}`

- 传入提示词来运行一个在当前工作目录的聊天会话：

`agy chat "{{提示词}}"`

- 安装或卸载特定扩展：

`agy --{{install|uninstall}}-extension {{发布者.扩展|路径/到/扩展.vsix}}`

- 向用户配置文件添加 MCP（Model Context Protocol）服务器定义：

`agy --add-mcp "{{json_字符串}}"`

- 显示帮助：

`agy {{[-h|--help]}}`

# x

> 用于管理模块和软件包。
> 更多信息：<https://x-cmd.com>。

- 使用特定模块（例如 path 模块）：

`x {{module}}`

- 全局安装一个软件包（例如 jq）：

`x env use {{package}}`

- 在当前 Shell 会话中临时尝试软件包：

`x env try {{package}}`

- 无需安装直接使用软件包：

`x {{package}}`

- 初始化 OpenAI API 密钥以使用 AI 功能：

`x openai init`

- 查询包的安装方法并执行：

`x install`

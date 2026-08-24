# codex

> 由 OpenAI 驱动的终端自然语言代码助手。
> 读取并编辑当前目录中的文件以完成请求。
> 更多信息：<https://developers.openai.com/codex/cli/reference>。

- 在当前目录中启动交互式 Codex 会话：

`codex`

- 使用提示词运行单个 Codex 命令：

`codex "{{提示词}}"`

- 运行提示词，允许 Codex 编辑工作区中的文件：

`codex --sandbox workspace-write "{{提示词}}"`

- 使用特定模型：

`codex {{[-m|--model]}} {{模型名称}} "{{提示词}}"`

- 使用本地开源模型提供商：

`codex --oss --local-provider {{lmstudio|ollama}} "{{提示词}}"`

- [交互式] 显示会话配置和词元使用情况：

`/status`

- 显示帮助：

`codex {{[-h|--help]}}`

# qwen

> 使用 Qwen3-Coder 启动一个交互式提示。
> 请参阅：`gemini`.
> 更多信息：<https://github.com/QwenLM/qwen-code>。

- 启动一个 REPL 会话以进行交互式对话：

`qwen`

- 将另一个命令的输出发送给 Qwen 并立即退出：

`{{echo "总结罗马的历史"}} | qwen {{[-p|--prompt]}}`

- 覆盖默认模型（默认值：qwen3-coder-max）：

`qwen {{[-m|--model]}} {{model_name}}`

- 在沙盒容器中运行：

`qwen {{[-s|--sandbox]}}`

- 执行一个提示，然后保持在交互模式中：

`qwen {{[-i|--prompt-interactive]}} "{{给我一个 Python 中递归的示例}}"`

- 在上下文中包含所有文件：

`qwen {{[-a|--all-files]}}`

- 在状态栏中显示内存使用情况：

`qwen --show-memory-usage`

# tgpt

> 无需 API 密钥即可与 AI 聊天机器人交谈。
> 可用提供者：`openai`、`opengpts`、`koboldai`、`phind`、`llama2`、`blackboxai`。
> 更多信息：<https://github.com/aandrew-me/tgpt>.

- 与默认提供者（GPT-3.5-turbo）聊天：

`tgpt "{{prompt}}"`

- 启动多行交互模式：

`tgpt {{[-m|--multiline]}}`

- 生成图像并保存到当前目录：

`tgpt {{[-img|--image]}} "{{prompt}}"`

- 用默认提供者（GPT-3.5-turbo）生成代码：

`tgpt {{[-c|--code]}} "{{prompt}}"`

- 安静地（不显示动画）与特定提供者聊天：

`tgpt --provider {{openai|opengpts|koboldai|phind|llama2|blackboxai}} {{[-q|--quiet]}} {{[-w|--whole]}} "{{prompt}}"`

- 使用特定提供者生成并执行 shell 命令（带确认提示）：

`tgpt --provider {{llama2}} {{[-s|--shell]}} "{{prompt}}"`

- 使用 API 密钥、模型、最大响应长度、温度和 `top_p` 参数进行提示（仅在使用 `openai` 提供者时需要）：

`tgpt --provider openai --key "{{api_key}}" --model "{{gpt-3.5-turbo}}" --max-length {{10}} --temperature {{0.7}} --top_p {{0.9}} "{{prompt}}"`

- 以文件作为额外的预提示输入：

`tgpt --provider {{blackboxai}} "{{prompt}}" < {{path/to/file}}`
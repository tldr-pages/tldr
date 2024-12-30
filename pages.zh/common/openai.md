# openai

> 命令行工具，提供对 OpenAI API 的访问。
> 更多信息：<https://github.com/openai/openai-python>。

- 列出模型：

`openai api models.list`

- 创建完成：

`openai api completions.create --model {{ada}} --prompt "{{Hello world}}"`

- 创建聊天完成：

`openai api chat_completions.create --model {{gpt-3.5-turbo}} --message {{user "Hello world"}}`

- 通过 DALL·E API 生成图像：

`openai api image.create --prompt "{{two dogs playing chess, cartoon}}" --num-images {{1}}`
# chatgpt

> 用于从终端使用 OpenAI 的 ChatGPT 和 DALL-E 的 Shell 脚本。
> 更多信息：<https://github.com/0xacx/chatGPT-shell-cli>.

- 以聊天模式启动：

`chatgpt`

- 提供一个提示以获取回答：

`chatgpt {{[-p|--prompt]}} "{{什么是匹配电子邮件地址的正则表达式？}}"`

- 使用特定模型以聊天模式启动（默认为 `gpt-3.5-turbo`）：

`chatgpt {{[-m|--model]}} {{gpt-4}}`

- 以聊天模式启动并使用初始提示：

`chatgpt {{[-i|--init-prompt]}} "{{你是 Rick，来自《Rick and Morty》。用他的风格回答问题并包含侮辱性的笑话。}}"`

- 将命令的结果作为提示传递给 `chatgpt`：

`echo "{{如何在 Ubuntu 上查看运行中的进程？}}" | chatgpt`

- 使用 DALL-E 生成图像：

`chatgpt {{[-p|--prompt]}} "{{image: 一只白色的猫}}"`
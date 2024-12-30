# chatgpt

> Shell脚本用于从终端使用OpenAI的ChatGPT和DALL-E。
> 更多信息：<https://github.com/0xacx/chatGPT-shell-cli>。

- 以聊天模式开始：

`chatgpt`

- 提供一个[p]rompt进行回答：

`chatgpt --prompt "{{匹配电子邮件地址的正则表达式是什么？}}"`

- 使用特定[m]odel以聊天模式开始（默认是`gpt-3.5-turbo`）：

`chatgpt --model {{gpt-4}}`

- 以[i]nitial prompt开始聊天模式：

`chatgpt --init-prompt "{{你是瑞克，来自《瑞克与莫蒂》。用他的风格回答问题，并包括侮辱性的笑话。}}"`

- 将命令的结果通过管道传递给`chatgpt`作为提示：

`echo "{{如何查看Ubuntu上运行的进程？}}" | chatgpt`

- 使用DALL-E生成图像：

`chatgpt --prompt "{{image: 一只白猫}}"`
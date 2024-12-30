# llm

> 通过远程 API 与大型语言模型（LLM）进行交互，或使用可以在本地计算机上安装和运行的模型。
> 更多信息：<https://llm.datasette.io/en/stable/help.html>。

- 设置 OpenAI API 密钥：

`llm keys set openai`

- 运行提示：

`llm "{{给宠物鹈鹕起十个有趣的名字}}"`

- 针对文件运行 [s]ystem 提示：

`cat {{path/to/file.py}} | llm --system "{{解释这段代码}}"`

- 将 PyPI 中的包安装到与 LLM 相同的环境中：

`llm install {{package1 package2 ...}}`

- 下载并针对 [m]odel 运行提示：

`llm --model {{orca-mini-3b-gguf2-q4_0}} "{{法国的首都是什么？}}"`

- 创建 [s]ystem 提示并使用模板名称保存它：

`llm --system '{{你是一个有意识的奶酪蛋糕}}' --save {{sentient_cheesecake}}`

- 使用特定 [m]odel 和特定 [t]emplate 进行互动聊天：

`llm chat --model {{chatgpt}} --template {{sentient_cheesecake}}`
# llm

> 通过远程 API 与大型语言模型 (LLMs) 交互，或安装并运行在本地机器上的模型。
> 更多信息：<https://llm.datasette.io/en/stable/help.html>.

- 设置 OpenAI API 密钥：

`llm keys set openai`

- 运行一个提示：

`llm "{{为一只鹈鹕起十个有趣的名字}}"`

- 对文件运行系统提示：

`cat {{path/to/file.py}} | llm {{[-s|--system]}} "{{解释这段代码}}"`

- 从 PyPI 安装包到与 LLM 相同的环境中：

`llm install {{package1 package2 ...}}`

- 下载并针对模型运行提示：

`llm {{[-m|--model]}} {{orca-mini-3b-gguf2-q4_0}} "{{法国的首都是什么？}}"`

- 创建系统提示并保存为模板：

`llm {{[-s|--system]}} '{{你是一个有意识的芝士蛋糕}}' --save {{sentient_cheesecake}}`

- 使用特定模型和特定模板进行交互式聊天：

`llm chat {{[-m|--model]}} {{chatgpt}} {{[-t|--template]}} {{sentient_cheesecake}}`
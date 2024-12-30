# tgpt

> 无需API密钥即可与AI聊天机器人交谈。
> 可用的提供者：`openai`、`opengpts`、`koboldai`、`phind`、`llama2`、`blackboxai`。
> 更多信息：<https://github.com/aandrew-me/tgpt>。

- 与默认提供者（GPT-3.5-turbo）聊天：

`tgpt "{{prompt}}"`

- 开始[m]ulti-line交互模式：

`tgpt --multiline`

- 生成[i]mages并将其保存到当前目录：

`tgpt --image "{{prompt}}"`

- 使用默认提供者（GPT-3.5-turbo）生成[c]ode：

`tgpt --code "{{prompt}}"`

- 安静地与特定提供者[q]uietly聊天（无动画）：

`tgpt --provider {{openai|opengpts|koboldai|phind|llama2|blackboxai}} --quiet --whole "{{prompt}}"`

- 使用特定提供者生成并执行[s]hell命令（带确认提示）：

`tgpt --provider {{llama2}} --shell "{{prompt}}"`

- 使用API密钥、模型、最大响应长度、温度和`top_p`进行提示（在使用`openai`提供者时必需）：

`tgpt --provider openai --key "{{api_key}}" --model "{{gpt-3.5-turbo}}" --max-length {{10}} --temperature {{0.7}} --top_p {{0.9}} "{{prompt}}"`

- 将文件作为附加预提示输入：

`tgpt --provider {{blackboxai}} "{{prompt}}" < {{path/to/file}}`
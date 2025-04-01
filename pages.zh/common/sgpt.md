# sgpt

> 一个基于 OpenAI 的 GPT 模型的命令行生产力工具。
> 更多信息：<https://github.com/TheR1D/shell_gpt#readme>.

- 用作搜索引擎，询问太阳的质量：

`sgpt "{{太阳的质量}}"`

- 执行 Shell 命令，将当前目录中的所有文件设置为只读：

`sgpt --shell "{{将当前目录中的所有文件设置为只读}}"`

- 生成代码，解决经典的 Fizz Buzz 问题：

`sgpt --code "{{使用 Python 解决 Fizz Buzz 问题}}"`

- 使用唯一会话名称开始聊天会话：

`sgpt --chat {{会话名称}} "{{请记住我最喜欢的数字：4}}"`

- 开始一个 `REPL`（读取-求值-打印循环）会话：

`sgpt --repl {{命令}}`

- 显示帮助：

`sgpt --help`

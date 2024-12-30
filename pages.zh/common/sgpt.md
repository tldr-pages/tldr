# sgpt

> 由OpenAI的GPT模型驱动的命令行生产力工具。
> 更多信息：<https://github.com/TheR1D/shell_gpt#readme>。

- 将其用作搜索引擎，询问太阳的质量：

`sgpt "{{太阳的质量}}"`

- 执行Shell命令，并将当前目录下的所有文件应用`chmod 444`权限：

`sgpt --shell "{{将当前目录下所有文件设为只读}}"`

- 生成代码，解决经典的Fizz Buzz问题：

`sgpt --code "{{使用Python解决Fizz Buzz问题}}"`

- 以唯一的会话名称开始聊天会话：

`sgpt --chat {{会话名称}} "{{请记住我最喜欢的数字：4}}"`

- 开始一个`REPL`（读取-求值-输出循环）会话：

`sgpt --repl {{命令}}`

- 显示帮助信息：

`sgpt --help`
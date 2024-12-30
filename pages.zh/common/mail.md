# 邮件

> 如果没有给出参数，该命令将在用户的邮箱上操作。
> 要发送电子邮件，消息正文是从 `stdin` 构建的。
> 更多信息：<https://manned.org/mail>。

- 打开交互提示以检查个人邮件：

`mail`

- 发送一封带有可选抄送的邮件。下面的命令行在按下 `<Enter>` 后继续。输入消息文本（可以是多行）。按 `<Ctrl>-D` 完成消息文本：

`mail --subject="{{主题行}}" {{to_user@example.com}} --cc="{{抄送邮箱地址}}"`

- 发送包含文件内容的电子邮件：

`mail --subject="{{$HOSTNAME filename.txt}}" {{to_user@example.com}} < {{path/to/filename.txt}}`

- 发送一个 `tar.gz` 文件作为附件：

`tar cvzf - {{path/to/directory1 path/to/directory2}} | uuencode {{data.tar.gz}} | mail --subject="{{主题行}}" {{to_user@example.com}}`
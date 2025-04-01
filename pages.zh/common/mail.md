# mail

> 如果未给出参数，命令将操作用户的邮箱。
> 若要发送邮件，消息正文从 `stdin` 构建。
> 更多信息：<https://manned.org/mail>.

- 打开交互式提示以检查个人邮件：

`mail`

- 发送带有可选抄送的键入邮件消息。按下 `<Enter>` 后，命令行继续。输入消息文本（可以是多行）。按下 `<Ctrl d>` 以完成消息文本：

`mail --subject "{{主题行}}" {{to_user@example.com}} --cc "{{抄送邮箱地址}}"`

- 发送包含文件内容的邮件：

`mail --subject "{{$HOSTNAME filename.txt}}" {{to_user@example.com}} < {{path/to/filename.txt}}`

- 以附件形式发送 `tar.gz` 文件：

`tar cvzf - {{path/to/directory1 path/to/directory2}} | uuencode {{data.tar.gz}} | mail --subject "{{主题行}}" {{to_user@example.com}}`

- 显示帮助：

`mail {{[-h|--help]}}`

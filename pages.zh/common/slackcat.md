# slackcat

> 用于将文件和命令输出发送到 Slack 的工具。
> 更多信息：<https://github.com/bcicen/slackcat>.

- 将文件发送到 Slack：

`slackcat --channel {{channel_name}} {{path/to/file}}`

- 将文件以自定义文件名发送到 Slack：

`slackcat --channel {{channel_name}} --filename={{filename}} {{path/to/file}}`

- 将命令输出作为文本片段发送到 Slack：

`{{command}} | slackcat --channel {{channel_name}} --filename={{snippet_name}}`

- 持续将命令输出流式发送到 Slack：

`{{command}} | slackcat --channel {{channel_name}} --stream`
# emond

> 事件监控服务，接受来自各种服务的事件，通过简单的规则引擎处理这些事件，并采取相应的行动。
> 这些行动可以运行命令、发送电子邮件或短信。
> 更多信息：<https://keith.github.io/xcode-man-pages/emond.8.html>。

- 启动守护进程：

`emond`

- 通过指定文件或目录的路径为 emond 指定要处理的规则：

`emond -r {{path/to/file_or_directory}}`

- 使用特定的配置文件：

`emond -c {{path/to/config_file}}`
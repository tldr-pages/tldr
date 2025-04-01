# emond

> 事件监控服务，接受来自各种服务的事件，通过简单规则引擎进行处理，并采取行动。
> 可以运行命令、发送电子邮件或短信。
> 更多信息：<https://keith.github.io/xcode-man-pages/emond.8.html>。

- 启动守护进程：

`emond`

- 通过指定文件或目录的路径为 emond 提供处理规则：

`emond -r {{path/to/file_or_directory}}`

- 使用特定的配置文件：

`emond -c {{path/to/config_file}}`
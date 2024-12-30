# blackfire

> 监控、分析和测试 PHP 应用程序。
> 更多信息：<https://blackfire.io>。

- 初始化并配置 Blackfire 客户端：

`blackfire config`

- 启动 Blackfire 代理：

`blackfire agent`

- 在特定套接字上启动 Blackfire 代理：

`blackfire agent --socket="{{tcp://127.0.0.1:8307}}"`

- 在特定程序上运行分析器：

`blackfire run {{php path/to/file.php}}`

- 运行分析器并收集 10 个样本：

`blackfire --samples 10 run {{php path/to/file.php}}`

- 运行分析器并以 JSON 格式输出结果：

`blackfire --json run {{php path/to/file.php}}`

- 将分析文件上传到 Blackfire 网络服务：

`blackfire upload {{path/to/file}}`

- 查看 Blackfire 网络服务上分析的状态：

`blackfire status`
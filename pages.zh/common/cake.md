# cake

> CakePHP 框架的命令行处理器。
> 更多信息：<https://cakephp.org>。

- 显示有关当前应用的基本信息和可用命令：

`cake`

- 列出所有可用的路由：

`cake routes`

- 清除配置缓存：

`cake cache clear_all`

- 构建元数据缓存：

`cake schema_cache build --connection {{connection}}`

- 清除元数据缓存：

`cake schema_cache clear`

- 清除单个缓存表：

`cake schema_cache clear {{table_name}}`

- 启动开发用的 Web 服务器（默认端口为 8765）：

`cake server`

- 启动 REPL（交互式 shell）：

`cake console`
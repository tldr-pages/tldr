# zabbix_server

> Zabbix 软件的核心守护进程。
> 更多信息：<https://manned.org/zabbix_server>。

- 使用默认配置文件启动服务器：

`zabbix_server`

- 使用自定义配置文件启动服务器：

`zabbix_server {{[-c|--config]}} {{路径/到/zabbix_server.conf}}`

- 在前台运行服务器：

`zabbix_server {{[-c|--config]}} {{路径/到/zabbix_server.conf}} {{[-f|--foreground]}}`

- 测试配置文件并退出：

`zabbix_server {{[-c|--config]}} {{路径/到/zabbix_server.conf}} {{[-T|--test-config]}}`

- 重新加载配置缓存（运行时控制）：

`zabbix_server {{[-c|--config]}} {{路径/到/zabbix_server.conf}} {{[-R|--runtime-control]}} config_cache_reload`

- 执行 housekeeper（运行时控制）：

`zabbix_server {{[-c|--config]}} {{路径/到/zabbix_server.conf}} {{[-R|--runtime-control]}} housekeeper_execute`

- 增加或减少所有进程的日志级别（运行时控制）：

`zabbix_server {{[-c|--config]}} {{路径/到/zabbix_server.conf}} {{[-R|--runtime-control]}} log_level_{{increase|decrease}}`

- 显示帮助：

`zabbix_server {{[-h|--help]}}`

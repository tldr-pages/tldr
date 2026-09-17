# zabbix_agent2

> 用于监控服务器参数的守护进程。
> 更多信息：<https://manned.org/zabbix_agent2>。

- 使用默认配置文件启动代理：

`zabbix_agent2`

- 使用自定义配置文件启动代理：

`zabbix_agent2 {{[-c|--config]}} {{路径/到/zabbix_agent2.conf}}`

- 测试配置文件并退出：

`zabbix_agent2 {{[-c|--config]}} {{路径/到/zabbix_agent2.conf}} {{[-T|--test-config]}}`

- 测试指定监控项并输出详细信息：

`zabbix_agent2 {{[-c|--config]}} {{路径/到/zabbix_agent2.conf}} {{[-t|--test]}} {{监控项键值}} {{[-v|--verbose]}}`

- 从配置文件中重新加载用户参数（运行时控制）：

`zabbix_agent2 {{[-c|--config]}} {{路径/到/zabbix_agent2.conf}} {{[-R|--runtime-control]}} userparameter_reload`

- 增加或减少日志级别（运行时控制）：

`zabbix_agent2 {{[-c|--config]}} {{路径/到/zabbix_agent2.conf}} {{[-R|--runtime-control]}} loglevel {{increase|decrease}}`

- 显示帮助：

`zabbix_agent2 {{[-h|--help]}}`

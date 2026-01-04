# zabbix_agentd

> 用于监控服务器参数的守护进程。
> 更多信息：<https://manned.org/zabbix_agentd>。

- 使用默认配置文件启动 agent：

`zabbix_agentd`

- 使用自定义配置文件启动 agent：

`zabbix_agentd {{[-c|--config]}} {{路径/到/zabbix_agentd.conf}}`

- 在前台运行 agent（保持附着在当前终端会话中）：

`zabbix_agentd {{[-c|--config]}} {{路径/到/zabbix_agentd.conf}} {{[-f|--foreground]}}`

- 测试配置文件：

`zabbix_agentd {{[-c|--config]}} {{路径/到/zabbix_agentd.conf}} {{[-T|--test-config]}}`

- 使用详细输出测试指定的监控项：

`zabbix_agentd {{[-c|--config]}} {{路径/到/zabbix_agentd.conf}} {{[-t|--test]}} {{监控项键值}} {{[-v|--verbose]}}`

- 从配置文件重新加载用户参数（运行时控制）：

`zabbix_agentd {{[-c|--config]}} {{路径/到/zabbix_agentd.conf}} {{[-R|--runtime-control]}} userparameter_reload`

- 提高或降低所有进程的日志级别（运行时控制）：

`zabbix_agentd {{[-c|--config]}} {{路径/到/zabbix_agentd.conf}} {{[-R|--runtime-control]}} log_level_{{increase|decrease}}`

- 显示帮助信息：

`zabbix_agentd {{[-h|--help]}}`

# zabbix_agentd

> Daemon for monitoring server parameters.
> More information: <https://manned.org/zabbix_agentd>.

- Start the agent with the default configuration file:

`zabbix_agentd`

- Start the agent with a custom configuration file:

`zabbix_agentd {{[-c|--config]}} {{path/to/zabbix_agentd.conf}}`

- Run the agent in foreground (it stays attached to the current terminal session):

`zabbix_agentd {{[-c|--config]}} {{path/to/zabbix_agentd.conf}} {{[-f|--foreground]}}`

- Test the configuration file:

`zabbix_agentd {{[-c|--config]}} {{path/to/zabbix_agentd.conf}} {{[-T|--test-config]}}`

- Test a specific item with verbose output:

`zabbix_agentd {{[-c|--config]}} {{path/to/zabbix_agentd.conf}} {{[-t|--test]}} {{item_key}} {{[-v|--verbose]}}`

- Reload user parameters from the configuration file (runtime control):

`zabbix_agentd {{[-c|--config]}} {{path/to/zabbix_agentd.conf}} {{[-R|--runtime-control]}} userparameter_reload`

- Increase or decrease log level for all processes (runtime control):

`zabbix_agentd {{[-c|--config]}} {{path/to/zabbix_agentd.conf}} {{[-R|--runtime-control]}} log_level_{{increase|decrease}}`

- Display help:

`zabbix_agentd {{[-h|--help]}}`

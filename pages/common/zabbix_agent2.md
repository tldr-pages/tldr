# zabbix_agent2

> Daemon for monitoring server parameters.
> More information: <https://manned.org/zabbix_agent2>.

- Start the agent with the default configuration file:

`zabbix_agent2`

- Start the agent with a custom configuration file:

`zabbix_agent2 {{[-c|--config]}} {{path/to/zabbix_agent2.conf}}`

- Test the configuration file and exit:

`zabbix_agent2 {{[-c|--config]}} {{path/to/zabbix_agent2.conf}} {{[-T|--test-config]}}`

- Test a specific item with verbose output:

`zabbix_agent2 {{[-c|--config]}} {{path/to/zabbix_agent2.conf}} {{[-t|--test]}} {{item_key}} {{[-v|--verbose]}}`

- Reload user parameters from the configuration file (runtime control):

`zabbix_agent2 {{[-c|--config]}} {{path/to/zabbix_agent2.conf}} {{[-R|--runtime-control]}} userparameter_reload`

- Increase or decrease log level (runtime control):

`zabbix_agent2 {{[-c|--config]}} {{path/to/zabbix_agent2.conf}} {{[-R|--runtime-control]}} loglevel {{increase|decrease}}`

- Display help:

`zabbix_agent2 {{[-h|--help]}}`

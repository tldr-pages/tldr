# zabbix_server

> Core daemon of Zabbix software.
> More information: <https://manned.org/zabbix_server>.

- Start the server with the default configuration file:

`zabbix_server`

- Start the server with a custom configuration file:

`zabbix_server {{[-c|--config]}} {{path/to/zabbix_server.conf}}`

- Run the server in foreground:

`zabbix_server {{[-c|--config]}} {{path/to/zabbix_server.conf}} {{[-f|--foreground]}}`

- Test the configuration file and exit:

`zabbix_server {{[-c|--config]}} {{path/to/zabbix_server.conf}} {{[-T|--test-config]}}`

- Reload configuration cache (runtime control):

`zabbix_server {{[-c|--config]}} {{path/to/zabbix_server.conf}} {{[-R|--runtime-control]}} config_cache_reload`

- Execute the housekeeper (runtime control):

`zabbix_server {{[-c|--config]}} {{path/to/zabbix_server.conf}} {{[-R|--runtime-control]}} housekeeper_execute`

- Increase or decrease log level for all processes (runtime control):

`zabbix_server {{[-c|--config]}} {{path/to/zabbix_server.conf}} {{[-R|--runtime-control]}} log_level_{{increase|decrease}}`

- Display help:

`zabbix_server {{[-h|--help]}}`

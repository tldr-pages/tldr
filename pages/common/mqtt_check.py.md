# mqtt_check.py

> Simple utility for testing and validating MQTT login credentials.
> Part of the Impacket suite.
> More information: <https://github.com/fortra/impacket>.

- Check MQTT login credentials for a target (MQTT broker's hostname):

`mqtt_check.py {{domain}}/{{username}}:{{password}}@{{targetName}}`

- Specify a custom client ID for authentication:

`mqtt_check.py -client-id {{client_id}} {{domain}}/{{username}}:{{password}}@{{targetName}}`

- Enable SSL for the connection:

`mqtt_check.py -ssl {{domain}}/{{username}}:{{password}}@{{targetName}}`

- Connect to a specific port (default is 1883):

`mqtt_check.py -port {{port}} {{domain}}/{{username}}:{{password}}@{{targetName}}`

- Enable debug output:

`mqtt_check.py -debug {{domain}}/{{username}}:{{password}}@{{targetName}}`

- Display help:

`mqtt_check.py --help`

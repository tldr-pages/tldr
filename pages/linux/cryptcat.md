# cryptcat

> Cryptcat is netcat with encryption capabilities.
> More information: <http://cryptcat.sourceforge.net>.

- [l]isten on a specified [p]ort and print any data received:

`cryptcat -k {{password}} -l -p {{port}}`

- Connect to a certain port:

`cryptcat -k {{password}} {{ip_address}} {{port}}`

- Set a timeout [w]:

`cryptcat -k {{password}} -w {{timeout_in_seconds}} {{ip_address}} {{port}}`

- Scan [z] the open ports of a specified host:

`cryptcat -v -z {{ip_address}} {{port}}`

- Act as proxy and forward data from a local TCP port to the given remote host:

`cryptcat -k {{password}} -l -p {{local_port}} | cryptcat -k {{password}} {{hostname}} {{remote_port}}`

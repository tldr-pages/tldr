# rpcdump.py

> Dump remote RPC endpoints information via the Endpoint Mapper.
> Part of the Impacket suite.
> More information: <https://github.com/fortra/impacket>.

- Dump RPC endpoints using username and password:

`rpcdump.py {{domain}}/{{username}}:{{password}}@{{target}}`

- Dump RPC endpoints using NTLM hashes:

`rpcdump.py -hashes {{LMHASH}}:{{NTHASH}} {{domain}}/{{username}}:{{password}}@{{target}}`

- Specify a target IP address explicitly (useful if the target name is a NetBIOS name):

`rpcdump.py -target-ip {{target_ip}} {{domain}}/{{username}}:{{password}}@{{target}}`

- Connect to a specific port (default is 135 for RPC Endpoint Mapper):

`rpcdump.py -port {{port_number}} {{domain}}/{{username}}:{{password}}@{{target}}`

- Enable debug output:

`rpcdump.py -debug {{domain}}/{{username}}:{{password}}@{{target}}`

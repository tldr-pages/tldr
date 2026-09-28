# machine_role.py

> Determine the role of a remote Windows machine (e.g. domain controller, member server, or workstation).
> Part of the Impacket suite.
> More information: <https://github.com/fortra/impacket>.

- Determine the role of a machine using a username and password:

`machine_role.py {{domain}}/{{username}}:{{password}}@{{target}}`

- Determine the role using pass-the-hash authentication:

`machine_role.py -hashes {{LM_Hash}}:{{NT_Hash}} {{domain}}/{{username}}@{{target}}`

- Determine the role without prompting for a password (e.g. using an existing session):

`machine_role.py -no-pass {{domain}}/{{username}}@{{target}}`

- Determine the role using Kerberos authentication:

`machine_role.py -k {{domain}}/{{username}}@{{target}}`

- Specify the domain controller's IP address:

`machine_role.py -dc-ip {{ip_address}} {{domain}}/{{username}}:{{password}}@{{target}}`

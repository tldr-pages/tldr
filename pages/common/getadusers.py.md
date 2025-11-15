# GetADUsers.py

> Retrieve a list of users from Active Directory, including attributes like last logon timestamp and email.
> Part of the Impacket suite.
> More information: <https://github.com/fortra/impacket>.

- Enumerate all Active Directory users and their attributes:

`GetADUsers.py -all -dc-ip {{domain_controller_ip}} {{domain}}/{{username}}:{{password}}`

- Retrieve information only for a specific user:

`GetADUsers.py -user {{user}} -dc-ip {{domain_controller_ip}} {{domain}}/{{username}}:{{password}}`

- Extract user details using pass-the-hash authentication:

`GetADUsers.py -all -dc-ip {{domain_controller_ip}} -hashes {{LM_Hash}}:{{NT_Hash}} {{domain}}/{{username}}`

- Save output to a file:

`GetADUsers.py -all -dc-ip {{domain_controller_ip}} {{domain}}/{{username}}:{{password}} > {{path/to/output.txt}}`

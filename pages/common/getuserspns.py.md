# GetUserSPNs.py

> Retrieve Service Principal Names (SPNs) associated with Active Directory user accounts.
> Part of the Impacket suite.
> More information: <https://github.com/fortra/impacket>.

- Enumerate user accounts with an SPN and request their Kerberos TGS tickets:

`GetUserSPNs.py {{domain}}/{{username}}:{{password}} -dc-ip {{domain_controller_ip}}`

- Use pass-the-hash authentication:

`GetUserSPNs.py {{domain}}/{{username}} -hashes {{LM_Hash}}:{{NT_Hash}} -dc-ip {{domain_controller_ip}}`

- Save the output to a file:

`GetUserSPNs.py {{domain}}/{{username}}:{{password}} -dc-ip {{domain_controller_ip}} -outputfile {{output_file}}`

- Request only TGS tickets:

`GetUserSPNs.py {{domain}}/{{username}}:{{password}} -dc-ip {{domain_controller_ip}} -request`

- Request only TGS tickets using pass-the-hash authentication:

`GetUserSPNs.py {{domain}}/{{username}} -dc-ip {{domain_controller_ip}} -hashes {{LM_Hash}}:{{NT_Hash}} -request`

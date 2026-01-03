# rdp_check.py

> Test whether an account is valid on the target host using the RDP protocol (no full login, just authentication check).
> More information: <https://github.com/fortra/impacket>.

- Check if credentials are valid on a target (password prompted if omitted):

`rdp_check.py {{domain}}/{{username}}@{{target}}`

- Check credentials using NTLM hashes:

`rdp_check.py -hashes {{LM_Hash}}:{{NT_Hash}} {{domain}}/{{username}}@{{target}}`

- Check credentials with explicit password:

`rdp_check.py {{domain}}/{{username}}:{{password}}@{{target}}`

- Check credentials for a local account on the target (no domain):

`rdp_check.py {{username}}:{{password}}@{{target}}`

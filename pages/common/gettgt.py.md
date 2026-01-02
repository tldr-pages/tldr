# getTGT.py

> Request a Ticket Granting Ticket (TGT).
> More information: <https://github.com/fortra/impacket>.

- Request a TGT using a password:

`getTGT.py {{domain}}/{{username}}:{{password}}`

- Request a TGT using NTLM hashes:

`getTGT.py -hashes {{LM_Hash}}:{{NT_Hash}} {{domain}}/{{username}}`

- Use Kerberos authentication (from existing ccache, no password needed):

`getTGT.py -k -no-pass {{domain}}/{{username}}`

- Request a TGT using an AES key (128 or 256 bits):

`getTGT.py -aesKey {{aes_key}} {{domain}}/{{username}}`

- Specify a domain controller IP:

`getTGT.py -dc-ip {{domain_controller_ip}} {{domain}}/{{username}}:{{password}}`

- Request a service ticket directly (AS-REQ) for a specific SPN:

`getTGT.py -service {{SPN}} {{domain}}/{{username}}:{{password}}`

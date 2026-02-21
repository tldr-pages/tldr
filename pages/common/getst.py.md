# getST.py

> Request a Kerberos Service Ticket (TGS).
> Part of the Impacket suite.
> More information: <https://github.com/fortra/impacket>

- Request a service ticket for a specific SPN:

`getST.py {{domain}}/{{username}}:{{password}} -spn {{service}}/{{target}}`

- Request a ticket using NTLM hashes (pass-the-hash):

`getST.py -hashes {{LM_Hash}}:{{NT_Hash}} {{domain}}/{{username}} -spn {{service}}/{{target}}`

- Request a ticket using existing Kerberos ccache file:

`getST.py -no-pass -k {{domain}}/{{username}} -spn {{service}}/{{target}}`

- Impersonate another user via S4U2Self (requires delegation rights):

`getST.py -k -impersonate {{target_user}} {{domain}}/{{username}} -spn {{service}}/{{target}}`

- Force the ticket to be forwardable (Bronze Bit):

`getST.py -force-forwardable -k {{domain}}/{{username}} -spn {{service}}/{{target}}`

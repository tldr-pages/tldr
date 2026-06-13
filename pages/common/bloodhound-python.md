# bloodhound-python

> A Python ingestor for BloodHound, used to enumerate Active Directory relationships.
> More information: <https://github.com/dirkjanm/BloodHound.py#usage>.

- Collect all data using default collection methods (includes groups, sessions, and trusts):

`bloodhound-python --username {{username}} --password {{password}} --domain {{domain}}`

- Collect data using Kerberos authentication without requiring a plaintext password:

`bloodhound-python --collectionmethod {{All}} --kerberos --domain {{domain}}`

- Authenticate using NTLM hashes instead of a password:

`bloodhound-python --collectionmethod {{All}} --username {{username}} --hashes {{LM:NTLM}} --domain {{domain}}`

- Specify a custom name server for DNS queries:

`bloodhound-python --collectionmethod {{All}} --username {{username}} --password {{password}} --domain {{domain}} --nameserver {{nameserver}}`

- Save the output files as a compressed ZIP archive:

`bloodhound-python --collectionmethod {{All}} --username {{username}} --password {{password}} --domain {{domain}} --zip`

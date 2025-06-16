# evil-winrm

> Windows Remote Management (WinRM) shell for pentesting.
> Once connected, we get a PowerShell prompt on the target host.
> More information: <https://github.com/Hackplayers/evil-winrm>.

- Connect to a host:

`evil-winrm {{[-i|--ip]}} {{ip}} {{[-u|--user]}} {{user}} {{[-p|--password]}} {{password}}`

- Connect to a host using pass-the-hash authentication instead of a password:

`evil-winrm {{[-i|--ip]}} {{ip}} {{[-u|--user]}} {{user}} {{[-H|--hash]}} {{nt_hash}}`

- Connect to a host, specifying directories for PowerShell scripts and executables:

`evil-winrm {{[-i|--ip]}} {{ip}} {{[-u|--user]}} {{user}} {{[-p|--password]}} {{password}} {{[-s|--scripts]}} {{path/to/scripts}} {{[-e|--executables]}} {{path/to/executables}}`

- Connect to a host, using SSL:

`evil-winrm {{[-i|--ip]}} {{ip}} {{[-u|--user]}} {{user}} {{[-p|--password]}} {{password}} {{[-S|--ssl]}} {{[-c|--pub-key]}} {{path/to/pubkey}} {{[-k|--priv-key]}} {{path/to/privkey}}`

- Upload a file to the host:

`PS > upload {{path/to/local/file}} {{path/to/remote/file}}`

- List all loaded PowerShell functions:

`PS > menu`

- Load a PowerShell script from the `--scripts` directory:

`PS > {{script.ps1}}`

- Invoke a binary on the host from the `--executables` directory:

`PS > Invoke-Binary {{binary.exe}}`

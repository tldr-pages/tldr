# evil-winrm

> Windows Remote Management (WinRM) shell for pentesting.
> Once connected, we get a PowerShell prompt on the target host.
> More information: <https://github.com/Hackplayers/evil-winrm>.

- Connect to a host:

`evil-winrm --ip {{ip}} --user {{user}} --password {{password}}`

- Connect to a host, passing the password hash:

`evil-winrm --ip {{ip}} --user {{user}} --hash {{nt_hash}}`

- Connect to a host, specifying folders for scripts and executables:

`evil-winrm --ip {{ip}} --user {{user}} --password {{password}} --scripts {{path/to/scripts}} --executables {{path/to/executables}}`

- Connect to a host, using SSL:

`evil-winrm --ip {{ip}} --user {{user}} --password {{password}} --ssl --pub-key {{path/to/pubkey}} --priv-key {{path/to/privkey}}`

- Upload a file to the host:

`*Evil-WinRM* PS C:\Users\user\Documents> upload {{path/to/local/file}} {{path/to/remote/file}}`

- Get the list of loaded PowerShell functions:

`*Evil-WinRM* PS C:\Users\user\Documents> menu`

- Load a PowerShell script from the `--scripts` folder:

`*Evil-WinRM* PS C:\Users\user\Documents> {{script.ps1}}`

- Invoke a binary on the host from the `--executables` folder:

`*Evil-WinRM* PS C:\Users\user\Documents> Invoke-Binary {{binary.exe}}`

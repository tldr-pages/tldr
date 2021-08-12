# evil-winrm

> Windows Remote Management (WinRM) shell pentru pentesting.
> Odată conectat, primim un prompt PowerShell pe gazda țintă.
> Mai multe informaţii: <https://github.com/Hackplayers/evil-winrm>

- Conectează-te la o gazdă:

`evil-winrm --ip {{ip}} --user {{user}} --password {{password}}`

- Conectați-vă la o gazdă, trecând hash-ul parolei:

`evil-winrm --ip {{ip}} --user {{user}} --hash {{nt_hash}}`

- Conectați-vă la o gazdă, specificând directoare pentru scripturi și executabile:

`evil-winrm --ip {{ip}} --user {{user}} --password {{password}} --scripts {{path/to/scripts}} --executables {{path/to/executables}}`

- Conectează-te la o gazdă, folosind SSL:

`evil-winrm --ip {{ip}} --user {{user}} --password {{password}} --ssl --pub-key {{path/to/pubkey}} --priv-key {{path/to/privkey}}`

- Încărcați un fișier la gazdă:

`PS > upload {{path/to/local/file}} {{path/to/remote/file}}`

- Obțineți o listă de funcții PowerShell încărcate:

`PS > menu`

- Încărcați un script PowerShell din directorul `—scripts`:

`PS > {{script.ps1}}`

- Invocați un binar pe gazdă din directorul `—executabil`:

`PS > Invoke-Binary {{binary.exe}}`

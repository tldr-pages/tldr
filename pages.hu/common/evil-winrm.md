# evil-winrm

> Windows Remote Management (WinRM) shell a penteszteléshez. A csatlakozást követően PowerShell promptot kapunk a célállomáson. További információ: <https://github.com/Hackplayers/evil-winrm>.

- Csatlakozás egy állomáshoz:

`evil-winrm --ip {{ip}} --user {{user}} --password {{password}}`

- Csatlakozás egy állomáshoz, a jelszó hash átadásával:

`evil-winrm --ip {{ip}} --user {{user}} --hash {{nt_hash}}`

- Csatlakozás egy állomáshoz, könyvtárak megadása a szkriptek és futtatható fájlok számára:

`evil-winrm --ip {{ip}} --user {{user}} --password {{password}} --scripts {{path/to/scripts}} --executables {{path/to/executables}}`

- Csatlakozás egy állomáshoz, SSL használatával:

`evil-winrm --ip {{ip}} --user {{user}} --password {{password}} --ssl --pub-key {{path/to/pubkey}} --priv-key {{path/to/privkey}}`

- Fájl feltöltése a hosztra:

`PS > upload {{path/to/local/file}} {{path/to/remote/file}}`

- A betöltött PowerShell-funkciók listájának lekérdezése:

`PS > menu`

- PowerShell szkript betöltése a `--scripts` könyvtárból:

`PS > {{script.ps1}}`

- Egy bináris program meghívása az állomáson a `--executables` könyvtárból:

`PS > Invoke-Binary {{binary.exe}}`

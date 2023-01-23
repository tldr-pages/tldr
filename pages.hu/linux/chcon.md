# chcon

> Egy fájl vagy fájlok/könyvtárak SELinux biztonsági környezetének módosítása. További információ: <https://www.gnu.org/software/coreutils/chcon>.

- Egy fájl biztonsági környezetének megtekintése:

`ls -lZ {{path/to/file}}`

- Egy célfájl biztonsági környezetének módosítása egy referenciafájl segítségével:

`chcon --reference={{reference_file}} {{target_file}}`

- Egy fájl teljes SELinux biztonsági környezetének módosítása:

`chcon {{user}}:{{role}}:{{type}}:{{range/level}} {{filename}}`

- A SELinux biztonsági környezetnek csak a felhasználói részének módosítása:

`chcon -u {{user}} {{filename}}`

- A SELinux biztonsági környezetnek csak a szerepkör részét módosíthatja:

`chcon -r {{role}} {{filename}}`

- A SELinux biztonsági környezetnek csak a típus részét módosíthatja:

`chcon -t {{type}} {{filename}}`

- A SELinux biztonsági környezetnek csak a tartomány/szint részének módosítása:

`chcon -l {{range/level}} {{filename}}`

# msiexec

> Windows programok telepítése, frissítése, javítása vagy eltávolítása MSI és MSP csomagfájlok segítségével. További információ: <https://learn.microsoft.com/windows-server/administration/windows-commands/msiexec>.

- Program telepítése az MSI-csomagból:

`msiexec /package {{path/to/file.msi}}`

- MSI csomag telepítése egy weboldalról:

`msiexec /package {{https://example.com/installer.msi}}`

- MSP javítófájl telepítése:

`msiexec /update {{path/to/file.msp}}`

- Egy program vagy javítófolt eltávolítása a megfelelő MSI- vagy MSP-fájl segítségével:

`msiexec /uninstall {{path/to/file}}`

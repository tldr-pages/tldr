# wsl

> A Windows Subsystem for Linux kezelése a parancssorból. További információ: <https://learn.microsoft.com/windows/wsl/reference>.

- Indítson el egy Linux shell-t (az alapértelmezett disztribúcióban):

`wsl {{shell_command}}`

- Linux-parancs futtatása shell használata nélkül:

`wsl --exec {{command}} {{command_arguments}}`

- Adjon meg egy adott disztribúciót:

`wsl --distribution {{distribution}} {{shell_command}}`

- Az elérhető disztribúciók listázása:

`wsl --list`

- Egy disztribúció exportálása a `.tar` fájlba:

`wsl --export {{distribution}} {{path/to/distro_fs.tar}}`

- Disztribúció importálása a `.tar` fájlból:

`wsl --import {{distribution}} {{path/to/install_location}} {{path/to/distro_fs.tar}}`

- A megadott disztribúcióhoz használt wsl verziójának módosítása:

`wsl --set-version {{distribution}} {{version}}`

- A Windows Subsystem for Linux leállítása:

`wsl --shutdown`

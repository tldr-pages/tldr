# fdesetup

> Establece y recupera información relacionada con FileVault.
> Más información: <https://keith.github.io/xcode-man-pages/fdesetup.8.html>.

- Lista los usuarios actuales habilitados para FileVault:

`sudo fdesetup list`

- Obtén el estado actual de FileVault:

`fdesetup status`

- Añade un usuario habilitado para FileVault:

`sudo fdesetup add -usertoadd {{usuario1}}`

- Habilita FileVault:

`sudo fdesetup enable`

- Desactiva FileVault:

`sudo fdesetup disable`

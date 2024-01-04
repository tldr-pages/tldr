# fdesetup

> Establece y recupera información relacionada con FileVault.
> Más información: <https://www.unix.com/man-page/mojave/8/fdesetup/>.

- Lista los usuarios actuales habilitados para FileVault:

`sudo fdesetup list`

- Obtiene el estado actual de FileVault:

`fdesetup status`

- Añade un usuario habilitado para FileVault:

`sudo fdesetup add -usertoadd {{usuario1}}`

- Habilita FileVault:

`sudo fdesetup enable`

- Desactiva FileVault:

`sudo fdesetup disable`

# aurman

> Un utilitar Arch Linux pentru a construi și instala pachete din Arch User Repository.
> A se vedea, de asemenea, „pacman”.
> Mai multe informaţii: <https://github.com/polygamma/aurman>

- Sincronizați și actualizați toate pachetele:

`aurman --sync --refresh --sysupgrade`

- Sincronizați și actualizați toate pachetele fără a afișa modificări ale fișierelor `PKGBUILD `:

`aurman --sync --refresh --sysupgrade --noedit`

- Instalați un pachet nou:

`aurman --sync {{package_name}}`

- Instalați un pachet nou fără a afișa modificări ale fișierelor `PKGBUILD `:

`aurman --sync --noedit {{package_name}}`

- Instalați un pachet nou fără a solicita:

`aurman --sync --noedit --noconfirm {{package_name}}`

- Căutați în baza de date a pachetelor un cuvânt cheie din depozitele oficiale și AUR:

`aurman --sync --search {{keyword}}`

- Eliminați un pachet și dependențele sale:

`aurman --remove --recursive --nosave {{package_name}}`

- Ștergeți memoria cache a pachetului (utilizați două steaguri `—clean pentru a curăța toate pachetele):

`aurman --sync --clean`

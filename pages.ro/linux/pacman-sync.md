# pacman --sync

> Arch Linux pachet manager utilitar.
> Mai multe informaţii: <https://man.archlinux.org/man/pacman.8>

- Instalați un pachet nou:

`sudo pacman --sync {{package_name}}`

- Sincronizați și actualizați toate pachetele (adăugați `—downloadonly` pentru a descărca pachetele și nu le actualiza):

`sudo pacman --sync --refresh --sysupgrade`

- Actualizați toate pachetele și instalați unul nou fără a solicita:

`sudo pacman --sync --refresh --sysupgrade --noconfirm {{package_name}}`

- Căutați în baza de date a pachetelor o expresie sau un cuvânt cheie regulat:

`pacman --sync --search "{{search_pattern}}"`

- Afișează informații despre un pachet:

`pacman --sync --info {{package_name}}`

- Suprascrie fișierele conflictuale în timpul unei actualizări pachet:

`sudo pacman --sync --refresh --sysupgrade --overwrite {{path/to/file}}`

- Sincronizați și actualizați toate pachetele, dar ignorați un anumit pachet (poate fi folosit de mai multe ori):

`sudo pacman --sync --refresh --sysupgrade --ignore {{package_name}}`

- Eliminați pachetele neinstalate și depozitele neutilizate din memoria cache (utilizați două semnalizatoare `—clean` pentru a curăța toate pachetele):

`sudo pacman --sync --clean`

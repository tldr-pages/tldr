# pacaur

> Un utilitar pentru Arch Linux pentru a construi și instala pachete din depozitul de utilizatori Arch.

- Sincronizați și actualizați toate pachetele (include AUR):

`pacaur -Syu`

- Sincronizați și actualizați numai pachetele AUR:

`pacaur -Syua`

- Instalați un pachet nou (include AUR):

`pacaur -S {{package_name}}`

- Elimină un pachet și dependențele sale (include pachete AUR):

`pacaur -Rs {{package_name}}`

- Caută în baza de date a pachetelor pentru un cuvânt cheie (include AUR):

`pacaur -Ss {{keyword}}`

- Listează toate pachetele instalate în prezent (include pachete AUR):

`pacaur -Qs`

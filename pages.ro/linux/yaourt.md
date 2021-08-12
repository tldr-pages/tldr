# yaourt

> Utilitarul Arch Linux pentru construirea pachetelor din depozitul de utilizatori Arch.

- Sincronizați și actualizați toate pachetele (inclusiv AUR):

`yaourt -Syua`

- Instalați un pachet nou (include AUR):

`yaourt -S {{package_name}}`

- Elimină un pachet și dependențele sale (include pachete AUR):

`yaourt -Rs {{package_name}}`

- Caută în baza de date a pachetelor un cuvânt cheie (inclusiv AUR):

`yaourt -Ss {{package_name}}`

- Lista pachetelor, versiunilor și depozitelor instalate (pachetele AUR vor fi listate sub numele de depozit „local”):

`yaourt -Q`

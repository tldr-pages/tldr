# yay

> Încă un alt iaurt: Un utilitar pentru Arch Linux pentru a construi și instala pachete din depozitul de utilizatori Arch.
> A se vedea, de asemenea, `pacman'.
> Mai multe informaţii: <https://github.com/Jguer/yay>

- Căutarea interactivă și instalarea pachetelor din repos și AUR:

`yay {{package_name|search_term}}`

- Sincronizați și actualizați toate pachetele din repos și AUR:

`yay`

- Sincronizați și actualizați numai pachetele AUR:

`yay -Sua`

- Instalați un nou pachet de repos și AUR:

`yay -S {{package_name}}`

- Eliminați un pachet instalat și atât dependențele sale și fișierele de configurare:

`yay -Rns {{package_name}}`

- Caută în baza de date a pachetelor pentru un cuvânt cheie din repos și AUR:

`yay -Ss {{keyword}}`

- Arată statistici pentru pachetele instalate și starea sistemului:

`yay -Ps`

# trizen

> Utilitar Arch Linux pentru construirea de pachete din Arch User Repository (AUR).
> Mai multe informaţii: <https://github.com/trizen/trizen>

- Sincronizați și actualizați toate pachetele AUR:

`trizen -Syua`

- Instalați un pachet nou:

`trizen -S {{package}}`

- Eliminați un pachet și dependențele sale:

`trizen -Rs {{package}}`

- Caută în baza de date a pachetelor pentru un cuvânt cheie:

`trizen -Ss {{keyword}}`

- Afișați informații despre un pachet:

`trizen -Si {{package}}`

- Lista pachetelor și versiunilor instalate:

`trizen -Qe`

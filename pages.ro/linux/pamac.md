# pamac

> Un utilitar de linie de comandă pentru managerul de pachete GUI pamac.
> Dacă nu vedeți pachetele AUR, activați-l în `/etc/pamac.conf` sau în GUI.
> Mai multe informaţii: <https://wiki.manjaro.org/index.php/Pamac>

- Instalați un pachet nou:

`pamac install {{package_name}}`

- Eliminați un pachet și dependențele sale nu mai sunt necesare (orfani):

`pamac remove --orphans {{package_name}}`

- Caută în baza de date a pachetelor pentru un pachet:

`pamac search {{package_name}}`

- Lista pachetelor instalate:

`pamac list --installed`

- Verificați actualizările pachetelor:

`pamac checkupdates`

- Upgrade toate pachetele:

`pamac upgrade`

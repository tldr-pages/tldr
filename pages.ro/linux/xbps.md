# xbps

> X Binary Package System (sau xbps) este sistemul binar de pachete folosit de Void Linux.
> Mai multe informaţii: <https://github.com/void-linux/xbps>

- Instalați pachetele și sincronizați-le cu depozitul de la distanță:

`xbps-install --synchronize {{package_name1}} {{package_name2}}`

- Căutați un pachet în depozitul de la distanță:

`xbps-query --repository -s {{package_name}}`

- Eliminați un pachet, lăsând toate dependențele sale instalate:

`xbps-remove {{package_name}}`

- Eliminați un pachet și toate dependențele sale recursiv care nu sunt cerute de alte pachete:

`xbps-remove --recursive {{package_name}}`

- Sincronizați bazele de date ale depozitului și actualizați sistemul și dependențele:

`xbps-install --synchronize -u`

- Eliminați pachetele care au fost instalate ca dependențe și care nu sunt necesare momentan:

`xbps-remove --remove-orphans`

- Eliminați pachetele învechite din memoria cache:

`xbps-remove --clean-cache`

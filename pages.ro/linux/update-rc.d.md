# update-rc.d

> Instalați și eliminați serviciile care sunt legăturile scriptului de inițializare System-V stil.
> Scripturile de inițializare sunt în `/etc/init.d/`.
> Mai multe informaţii: <https://manned.org/update-rc.d>

- Instalați un serviciu:

`update-rc.d {{mysql}} defaults`

- Activează un serviciu:

`update-rc.d {{mysql}} enable`

- Dezactivează un serviciu:

`update-rc.d {{mysql}} disable`

- Eliminați forțat un serviciu:

`update-rc.d -f {{mysql}} remove`

# file

> Determinați tipul fișierului.
> Mai multe informaţii: <https://manned.org/file>

- Dați o descriere a tipului fișierului specificat. Funcționează bine pentru fișiere fără extensie de fișier:

`file {{filename}}`

- Uită-te în interiorul unui fișier arhivat și determină tipul (tipurile) de fișier din interior:

`file -z {{foo.zip}}`

- Permiteți fișierului să lucreze cu fișiere speciale sau dispozitiv:

`file -s {{filename}}`

- Nu vă opriți la prima potrivire de tip fișier; continuați până la sfârșitul fișierului:

`file -k {{filename}}`

- Determinați tipul de codificare a unui fișier:

`file -i {{filename}}`

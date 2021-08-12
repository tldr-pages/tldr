# airmon-ng

> Activați modul monitor pe dispozitivele de rețea fără fir.
> Mai multe informaţii: <https://www.aircrack-ng.org/doku.php?id=airmon-ng>

- Lista dispozitivelor fără fir și stările acestora:

`sudo airmon-ng`

- Activați modul monitor pentru un anumit dispozitiv:

`sudo airmon-ng start {{wlan0}}`

- Omoară procesele deranjante care utilizează dispozitive fără fir:

`sudo airmon-ng check kill`

- Dezactivați modul monitor pentru o interfață de rețea specifică:

`sudo airmon-ng stop {{wlan0mon}}`

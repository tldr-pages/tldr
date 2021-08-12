# clamav

> Program antivirus cu sursă deschisă.
> Proiectat special pentru scanarea poştei electronice pe gateway-urile de poştă electronică, dar poate fi utilizat în alte contexte.
> Mai multe informaţii: <https://www.clamav.net>

- Actualizare definiții de viruși:

`freshclam`

- Scanați un fișier pentru viruși:

`clamscan {{path/to/file}}`

- Scanați directoarele recursiv și imprimați fișierele infectate:

`clamscan --recursive --infected {{path/to/directory}}`

- Scanaţi directoarele recursiv şi mutaţi-le în carantină:

`clamscan --recursive --move={{directory}}`

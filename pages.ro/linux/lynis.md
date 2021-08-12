# lynis

> Sistem și instrument de audit de securitate.
> Mai multe informaţii: <https://cisofy.com/documentation/lynis/>

- Verifică dacă Lynis e la zi:

`sudo lynis update info`

- Efectuați un audit de securitate al sistemului:

`sudo lynis audit system`

- Efectuați un audit de securitate al unui fișier Dockerfile:

`sudo lynis audit dockerfile {{path/to/dockerfile}}`

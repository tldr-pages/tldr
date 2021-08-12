# scanimage

> Scanați imagini cu API-ul Scanner Access Now Easy.
> Mai multe informaţii: <http://sane-project.org/man/scanimage.1.html>

- Lista scanerelor disponibile pentru a vă asigura că dispozitivul țintă este conectat și recunoscut:

`scanimage -L`

- Scanați o imagine și salvați-o într-un fișier:

`scanimage --format={{pnm|tiff|png|jpeg}} > {{path/to/new_image}}`

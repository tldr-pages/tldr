# systemctl edit

> Edita archivos de unidad de systemd.
> Más información: <https://www.freedesktop.org/software/systemd/man/systemctl.html#edit%20UNIT%E2%80%A6>.

- Superpone un archivo de unidad de forma no destructiva:

`sudo systemctl edit {{archivo_unidad}}`

- Edita un archivo de unidad:

`sudo systemctl edit {{archivo_unidad}} {{[-l|--full]}}`

- Crea un nuevo archivo de unidad:

`sudo systemctl edit {{archivo_unidad}} {{[-lf|--full --force]}}`

- Superpone un archivo de unidad de usuario:

`systemctl edit {{archivo_unidad}} --user`

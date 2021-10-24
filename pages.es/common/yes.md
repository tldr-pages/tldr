# yes

> Retorna algo repetidamente.
> Este comando es frecuentemente utilizado para aceptar todas las confirmaciones en comandos de instalación (como apt-get).
> Más información: <https://www.gnu.org/software/coreutils/yes>.

- Retornar repetidamente "mensaje":

`yes {{mensaje}}`

- Retornar repetidamente "y":

`yes`

- Aceptar todas las confirmaciones que muestre el comando `apt-get`:

`yes | sudo apt-get install {{programa}}`

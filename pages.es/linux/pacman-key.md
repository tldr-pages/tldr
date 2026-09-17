# pacman-key

> Script de encapsulado para GnuPG utilizado para gestionar el conjunto de claves de pacman.
> Vea también: `pacman`.
> Más información: <https://manned.org/pacman-key>.

- Inicializa el conjunto de claves de `pacman`:

`sudo pacman-key --init`

- Añade las claves predeterminadas de Arch Linux:

`sudo pacman-key --populate`

- Muestra las claves del portallaves público:

`pacman-key {{[-l|--list-keys]}}`

- Añade las claves especificadas:

`sudo pacman-key {{[-a|--add]}} {{ruta/al/archivo-de-claves.gpg}}`

- Recibe una clave de un servidor de claves:

`sudo pacman-key {{[-r|--recv-keys]}} "{{uid|name|email}}"`

- Muestra la huella digital de una clave específica:

`pacman-key {{[-f|--finger]}} "{{uid|name|email}}"`

- Firma una clave importada localmente:

`sudo pacman-key --lsign-key "{{uid|name|email}}"`

- Elimina una clave específica:

`sudo pacman-key {{[-d|--delete]}} "{{uid|name|email}}"`

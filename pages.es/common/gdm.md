# gdm

> El gestor de pantalla GNOME (GDM) sustituye al X Display Manager (XDM).
> Vea también: `gdm-binary`, `gdmsetup`, `gdm-stop`, `gdm-restart`, `gdm-safe-restart`.
> Más información: <https://manned.org/gdm>.

- Ejecuta la aplicación GNOME Display Manager:

`gdm`

- Evita que `gdm` se ejecute como un proceso de fondo daemon:

`gdm --nodaemon`

- Desactiva la gestión de `gdm` de los servidores X de consola local para entornos sin pantalla o remotos:

`gdm --no-console`

- Evita la desinfección de variables de entorno que comienzan con `$LD_`:

`gdm --preserve-ld-vars`

- Muestra la ayuda:

`gdm --help`

- Muestra la versión:

`gdm --version`

# arch

> Muestra el nombre de la arquitectura del sistema, o ejecuta un comando bajo una arquitectura diferente.
> Véase también: `uname`.
> Más información: <https://www.unix.com/man-page/osx/1/arch/>.

- Muestra la arquitectura del sistema:

`arch`

- Ejecuta un comando usando x86_64:

`arch -x86_64 "{{comando}}"`

- Ejecuta un comando usando arm:

`arch -arm64 "{{comando}}"`

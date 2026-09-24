# pacman --deptest

> Comprueba cada dependencia especificada y devuelve una lista de las dependencias que no están satisfechas actualmente en el sistema.
> Vea también: `pacman`.
> Más información: <https://manned.org/pacman.8>.

- Muestra los nombres de los paquetes de las dependencias que no están instaladas:

`pacman -T {{paquete1 paquete2 ...}}`

- Comprueba si el paquete instalado cumple con la versión mínima especificada:

`pacman -T "{{bash>=5}}"`

- Comprueba si hay instalada una versión posterior de un paquete:

`pacman -T "{{bash>5}}"`

- Muestra la ayuda:

`pacman -Th`

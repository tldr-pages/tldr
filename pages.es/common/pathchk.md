# pathchk

> Comprueba la validez y la portabilidad de las rutas de acceso.
> Más información: <https://www.gnu.org/software/coreutils/manual/html_node/pathchk-invocation.html>.

- Comprueba la validez de las rutas de acceso en el sistema actual:

`pathchk {{ruta1 ruta2 ...}}`

- Comprueba la validez de las rutas de acceso en una gama más amplia de sistemas compatibles con POSIX:

`pathchk -p {{ruta1 ruta2 ...}}`

- Comprueba la validez de las rutas en todos los sistemas compatibles con POSIX:

`pathchk {{[-p -P|--portability]}} {{ruta1 ruta2 ...}}`

- Comprueba únicamente si las rutas están vacías o comienzan por un guión (-):

`pathchk -P {{ruta1 ruta2 ...}}`

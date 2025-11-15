# autopkgtest

> Ejecuta pruebas sobre paquetes de Debian.
> Más información: <https://manpages.debian.org/bookworm/autopkgtest/autopkgtest.1.en.html>.

- Construye el paquete en el directorio actual y ejecuta todas las pruebas directamente en el sistema:

`autopkgtest -- {{null}}`

- Ejecuta una prueba específica para el paquete en el directorio actual:

`autopkgtest --test-name={{nombre_de_prueba}} -- {{null}}`

- Descarga y construye un paquete específico con `apt-get`, luego ejecuta todas las pruebas:

`autopkgtest {{paquete}} -- {{null}}`

- Prueba el paquete en el directorio actual utilizando un nuevo directorio raíz:

`autopkgtest -- {{chroot}} {{ruta/a/nuevo/directorio}}`

- Prueba el paquete en el directorio actual sin reconstruirlo:

`autopkgtest {{[-B|--no-built-binaries]}} -- {{null}}`

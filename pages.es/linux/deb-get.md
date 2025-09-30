# deb-get

> Funcionalidad `apt-get` para paquetes `.deb` publicados en repositorios de terceros o a través de descarga directa.
> Funciona con distribuciones Linux que usan `apt-get`.
> Más información: <https://github.com/wimpysworld/deb-get>.

- Actualiza la lista de paquetes y versiones disponibles:

`deb-get update`

- Busca un paquete dado:

`deb-get search {{paquete}}`

- Muestra información sobre un paquete:

`deb-get show {{paquete}}`

- Instala un paquete o lo actualiza a la última versión disponible:

`deb-get install {{paquete}}`

- Elimina un paquete (utilizando `purge` en su lugar, también elimina sus archivos de configuración):

`deb-get remove {{paquete}}`

- Actualiza todos los paquetes instalados a sus versiones más recientes disponibles:

`deb-get upgrade`

- Lista todos los paquetes disponibles:

`deb-get list`

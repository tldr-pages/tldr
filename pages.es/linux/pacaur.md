# pacaur

> Utilidad de Arch Linux para construir e instalar paquetes del repositorio de usuarios de Arch.
> Más información: <https://github.com/rmarquis/pacaur#name>.

- Sincroniza y actualiza todos los paquetes (incluye AUR):

`pacaur -Syu`

- Sincroniza y actualiza solo los paquetes AUR:

`pacaur -Syua`

- Instala un nuevo paquete (incluye AUR):

`pacaur -S {{paquete}}`

- Elimina un paquete y sus dependencias (incluye paquetes AUR):

`pacaur -Rs {{paquete}}`

- Busca una palabra clave en la base de datos de paquetes (incluye AUR):

`pacaur -Ss {{palabra_clave}}`

- Lista todos los paquetes instalados en este momento (incluye paquetes AUR):

`pacaur -Qs`

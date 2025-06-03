# pacaur

> Utilidad de Arch Linux para construir e instalar paquetes del repositorio de usuarios de Arch.
> Más información: <https://github.com/rmarquis/pacaur>.

- Sincronice y actualice todos los paquetes (incluye AUR):

`pacaur -Syu`

- Sincronice y actualice solo los paquetes AUR:

`pacaur -Syua`

- Instale un nuevo paquete (incluye AUR):

`pacaur -S {{paquete}}`

- Elimine un paquete y sus dependencias (incluye paquetes AUR):

`pacaur -Rs {{paquete}}`

- Busque una palabra clave en la base de datos de paquetes (incluye AUR):

`pacaur -Ss {{palabra_clave}}`

- Liste todos los paquetes instalados en este momento (incluye paquetes AUR):

`pacaur -Qs`

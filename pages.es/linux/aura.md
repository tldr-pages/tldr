# aura

> El gestor de paquetes Aura: un gestor de paquetes seguro y multilingüe para Arch Linux y el AUR.
> Más información: <https://github.com/fosskers/aura>.

- Busca paquetes en los repositorios oficiales y AUR:

`aura --aursync --both --search {{palabra_clave|expresión_regular}}`

- Instala un paquete desde el AUR:

`aura --aursync {{paquete}}`

- Actualiza todos los paquetes del AUR en modo detallado y elimina todas las dependencias de construcción:

`aura --aursync --diff --sysupgrade --delmakedeps --unsuppress`

- Instala un paquete desde los repositorios oficiales:

`aura --sync {{paquete}}`

- Sincroniza y actualiza todos los paquetes desde los repositorios oficiales:

`aura --sync --refresh --sysupgrade`

- Reemplaza un paquete con uno más antiguo usando la caché de paquetes:

`aura --downgrade {{paquete}}`

- Elimina un paquete y sus dependencias:

`aura --remove --recursive --unneeded {{paquete}}`

- Elimina paquetes huérfanos (instalados como dependencias pero no requeridos por ningún paquete):

`aura --orphans --abandon`

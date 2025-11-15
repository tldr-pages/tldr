# vagrant box

> Administra cajas Vagrant (imágenes de máquinas virtuales).
> Vea también: `vagrant`.
> Más información: <https://developer.hashicorp.com/vagrant/docs/cli/box>.

- Lista todas las cajas instaladas:

`vagrant box list`

- Añade una nueva caja:

`vagrant box add {{hashicorp/bionic64}}`

- Añade una caja desde una URL personalizada:

`vagrant box add {{mi-caja}} {{https://example.com/mi-caja.box}}`

- Elimina una caja instalada:

`vagrant box remove {{hashicorp/bionic64}}`

- Actualiza todas las cajas que están en uso en el entorno Vagrant actual:

`vagrant box update`

- Actualiza una caja específica:

`vagrant box update --box {{bento/debian-12}}`

- Comprueba si hay una nueva versión disponible para la caja que está usando:

`vagrant box outdated`

- Limpia las versiones antiguas de las cajas instaladas:

`vagrant box prune`

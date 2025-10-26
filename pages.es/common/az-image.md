# az image

> Administra imagenes de máquinas virtuales personalizadas en Azure.
> Parte de `azure-cli` (también conocido como `az`).
> Más información: <https://learn.microsoft.com/cli/azure/image>.

- Lista imagenes personalizadas en un grupo de recursos:

`az image list {{[-g|--resource-group]}} {{grupo_recursos}}`

- Crea una imagen personalizada desde un disco existente o snapshots:

`az image create {{[-g|--resource-group]}} {{grupo_recursos}} {{[-n|--name]}} {{nombre}} --os-type {{windows|linux}} --source {{origen_disco_sistema_operativo}}`

- Elimina una imagen personalizada:

`az image delete {{[-n|--name]}} {{nombre}} {{[-g|--resource-group]}} {{grupo_recursos}}`

- Muestra detalles de una imagen personalizada:

`az image show {{[-n|--name]}} {{nombre}} {{[-g|--resource-group]}} {{grupo_recursos}}`

- Actualiza imagenes personalizadas:

`az image update {{[-n|--name]}} {{nombre}} {{[-g|--resource-group]}} {{grupo_recursos}} --set {{propiedad=valor}}`

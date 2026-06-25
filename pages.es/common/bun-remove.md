# bun remove

> Elimina una dependencia de `package.json`.
> Más información: <https://bun.com/docs/pm/cli/remove>.

- Elimina una dependencia:

`bun {{[rm|remove]}} {{nombre_del_paquete}}`

- Elimina varias dependencias:

`bun {{[rm|remove]}} {{nombre_del_paquete1 nombre_del_paquete2 ...}}`

- Elimina un paquete instalado globalmente:

`bun {{[rm|remove]}} {{[-g|--global]}} {{nombre_del_paquete}}`

- Elimina una dependencia sin actualizar el archivo `package.json`:

`bun {{[rm|remove]}} --no-save {{nombre_del_paquete}}`

- Ejecuta el comando sin eliminar realmente los paquetes (simular la eliminación):

`bun {{[rm|remove]}} --dry-run {{nombre_del_paquete}}`

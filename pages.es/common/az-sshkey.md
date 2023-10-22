# az sshkey

> Administra claves públicas SSH con máquinas virtuales.
> Parte de `azure-cli` (también conocido como `az`).
> Más información: <https://learn.microsoft.com/cli/azure/sshkey>.

- Crea una nueva clave SSH:

`az sshkey create --name {{nombre}} --resource-group {{grupo_de_recursos}}`

- Sube una clave SSH existente:

`az sshkey create --name {{nombre}} --resource-group {{grupo_de_recursos}} --public-key "{{@ruta/de/llave.pub}}"`

- Lista todas las claves públicas SSH:

`az sshkey list`

- Muestra información sobre una clave pública SSH:

`az sshkey show --name {{nombre}} --resource-group {{grupo_de_recursos}}`

# tart

> Crea, ejecuta y gestiona máquinas virtuales (VM) macOS y Linux en Apple Silicon.
> Más información: <https://github.com/cirruslabs/tart>.

- Extrae una imagen de VM remota:

`tart pull {{acme.io/org/nombre:tag}}`

- Clona una VM desde una fuente de imagen local o remota:

`tart clone {{source-vm}} {{nombre-vm}}`

- Crea una nueva Mac VM a partir de un archivo ipsw específico:

`tart create --from-ipsw={{ultima|ruta/al/archivo.ipsw}} {{nombre-de-la-vm}}`

- Ejecuta una máquina virtual existente:

`tart run {{nombre-de-la-vm}}`

- Ejecuta una máquina virtual existente con un directorio específico montado:

`tart run --dir={{ruta/al/directorio}}:{{ruta/a/directorio local}} {{nombre-de-la-vm}}`

- Lista máquinas virtuales:

`tart list`

- Obtiene la dirección IP de una máquina virtual en ejecución:

`tart ip {{nombre-de-la-vm}}`

- Cambia la resolución de pantalla de una máquina virtual:

`tart set {{nombre-de-la-vm}} --display {{640}}x{{400}}`

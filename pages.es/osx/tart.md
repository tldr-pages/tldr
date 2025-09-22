# tart

> Crea, ejecuta y gestiona máquinas virtuales (VM) macOS y Linux en Apple Silicon.
> Más información: <https://github.com/cirruslabs/tart>.

- Extrae una imagen de VM remota:

`tart pull {{acme.io/org/name:tag}}`

- Clona una VM desde una fuente de imagen local o remota:

`tart clone {{source-vm}} {{vm-name}}`

- Crea una nueva Mac VM a partir de un archivo ipsw específico:

`tart create --from-ipsw {{latest|path/to/file.ipsw}} {{vm-name}}`

- Ejecuta una máquina virtual existente:

`tart run {{vm-name}}`

- Ejecuta una máquina virtual existente con un directorio específico montado:

`tart run --dir {{path/to/directory}}:/{{path/to/local_directory}} {{vm-name}}`

- Lista máquinas virtuales:

`tart list`

- Obtén la dirección IP de una máquina virtual en ejecución:

`tart ip {{vm-name}}`

- Cambia la resolución de pantalla de una máquina virtual:

`tart set {{vm-name}} --display {{640}}x{{400}}`

# qm showcmd

> Muestra la línea de comandos que se utiliza para iniciar una máquina virtual (información de depuración).
> Más información: <https://pve.proxmox.com/pve-docs/qm.1.html>.

- Muestra la línea de comando inicial de una máquina virtual específica:

`qm showcmd {{id_mv}}`

- Pone cada opción en una nueva línea para mejorar la legibilidad:

`qm showcmd --pretty {{true}} {{id_mv}}`

- Obtiene valores de configuración de una instantánea específica:

`qm showcmd --snapshot {{cadena}} {{id_mv}}`

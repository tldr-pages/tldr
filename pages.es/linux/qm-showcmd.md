# qm showcmd

> Muestra la línea de comandos que se utiliza para iniciar una máquina virtual (información de depuración).
> Más información: <https://pve.proxmox.com/pve-docs/qm.1.html#cli_qm_showcmd>.

- Muestra la línea de comando inicial de una máquina virtual específica:

`qm {{[sho|showcmd]}} {{100}}`

- Pone cada opción en una nueva línea para mejorar la legibilidad:

`qm {{[sho|showcmd]}} --pretty {{true}} {{100}}`

- Obtiene valores de configuración de una instantánea específica:

`qm {{[sho|showcmd]}} --snapshot {{cadena}} {{100}}`

# qm guest

> Administra un agente invitado de máquina virtual.
> Más información: <https://pve.proxmox.com/pve-docs/qm.1.html#cli_qm_guest_cmd>.

- Imprime el estado de un PID específico:

`qm {{[g|guest]}} {{[exec-s|exec-status]}} {{id_mv}} {{pid}}`

- Establece una contraseña para un usuario específico en una máquina virtual de forma interactiva:

`qm {{[g|guest]}} {{[p|passwd]}} {{id_mv}} {{usuario}}`

- Establece una contraseña ya procesada (hashed) para un usuario específico en una máquina virtual de forma interactiva:

`qm {{[g|guest]}} {{[p|passwd]}} {{id_mv}} {{usuario}} --crypted 1`

- Ejecuta un comando específico de agente huésped en QEMU:

`qm {{[g|guest]}} {{[c|cmd]}} {{id_mv}} {{fsfreeze-freeze|fsfreeze-status|fsfreeze-thaw|fstrim|get-fsinfo|...}}`

- Ejecuta una orden específica a través de un agente huésped:

`qm {{[g|guest]}} exec {{id_mv}} {{comando}} {{primer_argumento segundo_argumento ...}}`

- Ejecuta una orden específica a través de un agente huésped asincrónicamente:

`qm {{[g|guest]}} exec {{id_mv}} {{primer_argumento segundo_argumento ...}} --synchronous 0`

- Ejecuta una orden específica a través de un agente huésped con un tiempo máximo de 10 segundos:

`qm {{[g|guest]}} exec {{id_mv}} {{primer_argumento segundo_argumento...}} --timeout {{10}}`

- Ejecuta una orden específica a través de un agente huésped y reenvía la entrada de `stdin` hasta el fin del archivo (EOF) al agente huésped:

`qm {{[g|guest]}} exec {{id_mv}} {{primer_argumento segundo_argumento ...}} --pass-stdin 1`

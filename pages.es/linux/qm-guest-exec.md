# qm guest exec

> Ejecuta una orden específica a través de un agente huésped.
> Más información: <https://pve.proxmox.com/pve-docs/qm.1.html>.

- Ejecuta una orden específica a través de un agente huésped:

`qm guest exec {{id_mv}} {{comando}} {{primer_argumento segundo_argumento ...}}`

- Ejecuta una orden específica a través de un agente huésped asincrónicamente:

`qm guest exec {{id_mv}} {{primer_argumento segundo_argumento ...}} --synchronous 0`

- Ejecuta una orden específica a través de un agente huésped con un tiempo máximo de 10 segundos:

`qm guest exec {{id_mv}} {{primer_argumento segundo_argumento...}} --timeout {{10}}`

- Ejecuta una orden específica a través de un agente huésped y reenvía la entrada de `stdin` hasta el fin del archivo (EOF) al agente huésped:

`qm guest exec {{id_mv}} {{primer_argumento segundo_argumento ...}} --pass-stdin 1`

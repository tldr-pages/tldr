# qm wait

> Espera hasta que se detenga la máquina virtual.
> Más información: <https://pve.proxmox.com/pve-docs/qm.1.html>.

- Espera hasta que se detenga la máquina virtual:

`qm wait {{id_mv}}`

- Espera hasta que la máquina virtual se detenga con un tiempo de espera máximo de 10 segundos:

`qm wait --timeout {{10}} {{id_mv}}`

- Envía una solicitud de apagado, luego espera hasta que la máquina virtual se detenga con un tiempo máximo de espera de 10 segundos:

`qm shutdown {{id_mv}} && qm wait --timeout {{10}} {{id_mv}}`

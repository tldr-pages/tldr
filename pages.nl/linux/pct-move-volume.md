# pct move-volume

> Verplaats een volume naar een andere opslag of naar een andere container.
> Meer informatie: <https://pve.proxmox.com/pve-docs/pct.1.html#cli_pct_move-volume>.

- Verplaats het rootbestandssysteem van een container naar een andere opslag:

`pct {{[mov|move-volume]}} {{100}} rootfs {{opslag_id}}`

- Verwijder de bestandssysteemkoppeling naar het oude volume zodra de verplaatsing is voltooid:

`pct {{[mov|move-volume]}} {{100}} rootfs {{opslag_id}} --delete`

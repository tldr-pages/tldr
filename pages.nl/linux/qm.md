# qm

> QEMU/KVM Virtual Machine Manager.
> Sommige subcommando's zoals `list`, `start`, `stop`, `clone`, etc. hebben hun eigen gebruiksdocumentatie.
> Meer informatie: <https://pve.proxmox.com/pve-docs/qm.1.html>.

- Toon alle virtual machines:

`qm list`

- Maak met behulp van een ISO-bestand dat is geüpload naar de lokale opslag een virtual machine met een 4 GB SCSI-schijf op de `local-lvm`-opslag en een ID van 100:

`qm {{[cr|create]}} {{100}} --scsi0 {{local-lvm:4}} --net0 {{e1000}} --cdrom {{local:iso/proxmox-mailgateway_2.1.iso}}`

- Toon de configuratie van een virtual machine, met vermelding van de ID:

`qm {{[co|config]}} {{100}}`

- Start een specifieke virtual machine:

`qm start {{100}}`

- Stuur een verzoek tot afsluiten en wacht vervolgens tot de virtual machine gestopt is:

`qm {{[shu|shutdown]}} {{100}} && qm {{[w|wait]}} {{100}}`

- Verwijder een virtual machine en al zijn gerelateerde bronnen:

`qm {{[des|destroy]}} {{100}} --purge`

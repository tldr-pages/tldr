# limactl

> Virtual machine manager voor Linux gasten, met meerdere VM templates beschikbaar.
> Kan worden gebruikt om containers op macOS uit te voeren, maar ook voor generieke virtuele machine use cases op macOS en Linux hosts.
> Meer informatie: <https://github.com/lima-vm/lima>.

- Toon VMs:

`limactl list`

- Maak een VM met standaard instellingen en voorzie optioneel van een naam en/of template (zie `limactl create --list-templates` voor beschikbare templates):

`limactl create --name {{vm_naam}} template://{{debian|fedora|ubuntu|...}}`

- Start een VM (dit kan enkele afhankelijkheden erin installeren en een paar minuten duren):

`limactl start {{vm_naam}}`

- Open een externe shell in een VM:

`limactl shell {{vm_naam}}`

- Voer een commando uit in een VM:

`limactl shell {{vm_naam}} {{commando}}`

- Stop/sluit een VM af:

`limactl stop {{vm_naam}}`

- Verwijder een VM:

`limactl remove {{vm_naam}}`

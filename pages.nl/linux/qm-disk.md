# qm disk

> Beheer schijf images.
> Meer informatie: <https://pve.proxmox.com/pve-docs/qm.1.html#cli_qm_disk_import>.

- Voeg `n` gigabytes toe aan een virtuele schijf:

`qm {{[di|disk]}} {{[resi|resize]}} {{vm_id}} {{schijf_naam}} +{{n}}G`

- Verplaats een virtuele schijf:

`qm {{[di|disk]}} {{[m|move]}} {{vm_id}} {{destination}} {{index}}`

- Verwijder de vorige kopie van de virtuele schijf:

`qm {{[di|disk]}} {{[m|move]}} --delete {{vm_id}} {{bestemming}} {{index}}`

- Importeer een VMDK/`.qcow2`/raw schijfimage met een specifieke opslagnaam:

`qm {{[di|disk]}} {{[i|import]}} {{vm_id}} {{pad/naar/schijf}} {{opslagnaam}} --format {{qcow2|raw|vmdk}}`

- Scan alle opslag opnieuw en update schijfgroottes en ongebruikte schijf images:

`qm {{[di|disk]}} {{[resc|rescan]}}`

- Voer een testscan uit en maak geen veranderingen in de configuraties:

`qm {{[di|disk]}} {{[resc|rescan]}} --dryrun`

- Specificeer een virtuele machine via zijn ID:

`qm {{[di|disk]}} {{[resc|rescan]}} --vmid {{100}}`

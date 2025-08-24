# qm disk rescan

> Scan alle opslag opnieuw en update schijfgroottes en ongebruikte schijf images van virtual machines.
> Meer informatie: <https://pve.proxmox.com/pve-docs/qm.1.html>.

- Scan alle opslag opnieuw en update schijfgroottes en ongebruikte schijf images:

`qm {{[di|disk]}} {{[resc|rescan]}}`

- Voer een testscan uit en maak geen veranderingen in de configuraties:

`qm {{[di|disk]}} {{[resc|rescan]}} --dryrun`

- Specificeer een virtual machine via zijn ID:

`qm {{[di|disk]}} {{[resc|rescan]}} --vmid {{100}}`

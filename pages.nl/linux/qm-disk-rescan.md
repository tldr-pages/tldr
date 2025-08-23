# qm disk rescan

> Scan alle opslag opnieuw en update schijfgroottes en ongebruikte schijf images van een virtual machine.
> Meer informatie: <https://pve.proxmox.com/pve-docs/qm.1.html>.

- Scan alle opslag opnieuw en update schijfgroottes en ongebruikte schijf images van een specifieke virtual machine:

`qm {{[di|disk]}} {{[resc|rescan]}}`

- Voer een testscan uit op een specifieke virtual machine en maak geen veranderingen in de configuraties:

`qm {{[di|disk]}} {{[resc|rescan]}} --dryrun`

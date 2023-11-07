# qm disk import

> Importeer een schijf image in een virtuele machine als een ongebruikte schijf.
> De onderstende image formaten voor `qemu-img`, zoals raw, qcow2, qed, vdi, vmdk, en vhd moeten gebruikt worden.
> Meer informatie: <https://pve.proxmox.com/pve-docs/qm.1.html>.

- Importeer een VMDK/qcow2/raw schijf image met behulp van een specifieke opslagnaam:

`qm importdisk {{vm_id}} {{pad/naar/schijf}} {{opslagnaam}} --format {{qcow2|raw|vmdk}}`

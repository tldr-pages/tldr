# virsh

> Gestionați domeniile de oaspeți virsh.
> NOTĂ: 'guest_id' poate fi ID-ul, numele sau UUID-ul oaspetelui.
> Mai multe informaţii: <https://libvirt.org/virshcmdref.html>

- Conectați-vă la o sesiune de hipervizor:

`virsh connect {{qemu:///system}}`

- Listează toate domeniile:

`virsh list --all`

- Dump fișier de configurare invitat:

`virsh dumpxml {{guest_id}} > {{path/to/guest.xml}}`

- Creați un oaspete dintr-un fișier de configurare:

`virsh create {{path/to/config_file.xml}}`

- Editați fișierul de configurare al unui oaspete (editorul poate fi modificat cu $EDITOR):

`virsh edit {{guest_id}}`

- Start/reboot/oprire/suspendare/reia un oaspete:

`virsh {{command}} {{guest_id}}`

- Salvați starea curentă a unui oaspete într-un fișier:

`virsh save {{guest_id}} {{filename}}`

- Ștergeți un oaspete care rulează:

`virsh destroy {{guest_id}} && virsh undefine {{guest_id}}`

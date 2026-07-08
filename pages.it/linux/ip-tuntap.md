# ip tuntap

> Gestisce le interfacce di rete virtuali TUN/TAP.
> Maggiori informazioni: <https://baturin.org/docs/iproute2/#ip-tuntap>.

- Mostra tutti i dispositivi TUN/TAP esistenti:

`ip {{[tunt|tuntap]}}`

- Crea un dispositivo TUN con un nome specifico:

`sudo ip {{[tunt|tuntap]}} {{[a|add]}} {{[d|dev]}} {{tun0}} {{[m|mode]}} {{[t|tun]}}`

- Crea un dispositivo TAP con un nome specifico:

`sudo ip {{[tunt|tuntap]}} {{[a|add]}} {{[d|dev]}} {{tap0}} {{[m|mode]}} {{[ta|tap]}}`

- Elimina un dispositivo TUN o TAP:

`sudo ip {{[tunt|tuntap]}} {{[d|delete]}} {{[d|dev]}} {{tun0|tap0}} {{[m|mode]}} {{tun|tap}}`

- Imposta il proprietario (UID) di un dispositivo TUN/TAP:

`sudo ip {{[tunt|tuntap]}} {{[a|add]}} {{[d|dev]}} {{tun0|tap0}} {{[m|mode]}} {{tun|tap}} {{[u|user]}} {{username}}`

- Imposta sia il proprietario (UID) che il gruppo (GID) per un dispositivo TUN/TAP:

`sudo ip {{[tunt|tuntap]}} {{[a|add]}} {{[d|dev]}} {{tun0|tap0}} {{[m|mode]}} {{tun|tap}} {{[u|user]}} {{username}} {{[g|group]}} {{group_name}}`

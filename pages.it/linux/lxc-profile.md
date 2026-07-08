# lxc profile

> Gestisce i profili per i container LXD.
> Maggiori informazioni: <https://documentation.ubuntu.com/lxd/latest/reference/manpages/lxc/profile/>.

- Elenca tutti i profili disponibili:

`lxc profile list`

- Mostra la configurazione di un profilo specifico:

`lxc profile show {{profile_name}}`

- Modifica un profilo specifico nell'editor predefinito:

`lxc profile edit {{profile_name}}`

- Modifica un profilo specifico importando i valori di configurazione da un file:

`lxc < {{config.yaml}} profile edit {{profile_name}}`

- Avvia un nuovo container con profili specifici:

`lxc launch {{container_image}} {{container_name}} {{[-p|--profile]}} {{profile1}} {{[-p|--profile]}} {{profile2}}`

- Cambia i profili di un container in esecuzione:

`lxc profile assign {{container_name}} {{profile1,profile2}}`

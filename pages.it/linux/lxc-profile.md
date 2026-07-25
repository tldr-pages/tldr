# lxc profile

> Gestisce i profili per i container LXD.
> Maggiori informazioni: <https://documentation.ubuntu.com/lxd/latest/reference/manpages/lxc/profile/>.

- Elenca tutti i profili disponibili:

`lxc profile list`

- Mostra la configurazione di un profilo specifico:

`lxc profile show {{nome_profilo}}`

- Modifica un profilo specifico nell'editor predefinito:

`lxc profile edit {{nome_profilo}}`

- Modifica un profilo specifico importando i valori di configurazione da un file:

`lxc < {{config.yaml}} profile edit {{nome_profilo}}`

- Avvia un nuovo container con profili specifici:

`lxc launch {{container_image}} {{nome_container}} {{[-p|--profile]}} {{profilo1}} {{[-p|--profile]}} {{profilo2}}`

- Cambia i profili di un container in esecuzione:

`lxc profile assign {{nome_container}} {{profilo1,profilo2}}`

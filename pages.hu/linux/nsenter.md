# nsenter

> Új parancs futtatása egy futó folyamat névterében. Különösen hasznos a docker image-ek vagy chroot jailek esetében. További információ: <https://manned.org/nsenter>.

- Egy adott parancs futtatása egy létező folyamat névterének felhasználásával:

`nsenter --target {{pid}} --all {{command}} {{command_arguments}}`

- Egy adott parancs futtatása egy meglévő folyamat hálózati névterében:

`nsenter --target {{pid}} --net {{command}} {{command_arguments}}`

- Egy adott parancs futtatása egy meglévő folyamat PID névterében:

`nsenter --target {{pid}} --pid {{command}} {{command_arguments}}`

- Egy adott parancs futtatása egy meglévő folyamat IPC névterében:

`nsenter --target {{pid}} --ipc {{command}} {{command_arguments}}`

- Egy adott parancs futtatása egy meglévő folyamat UTS, idő és IPC névterében:

`nsenter --target {{pid}} --uts --time --ipc -- {{command}} {{command_arguments}}`

- Egy adott parancs futtatása egy meglévő folyamat névterében a procfs-re való hivatkozással:

`nsenter --pid=/proc/{{pid}}/pid/net -- {{command}} {{command_arguments}}`

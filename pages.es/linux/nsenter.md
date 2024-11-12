# nsenter

> Ejecuta un nuevo comando en el espacio de nombres de un proceso en ejecución.
> Particularmente útil para imágenes Docker o jaulas chroot.
> Más información: <https://manned.org/nsenter>.

- Ejecuta un comando específico utilizando los mismos espacios de nombres como un proceso existente:

`nsenter --target {{pid}} --all {{comando}} {{argumentos_del_comando}}`

- Ejecuta un comando específico en el espacio de nombres mount|UTS|IPC|network|PID|user|cgroup|time de un proceso existente:

`nsenter --target {{pid}} --{{mount|uts|ipc|net|pid|user|cgroup}} {{comando}} {{argumentos_del_comando}}`

- Ejecuta un comando específico en los espacios de nombres UTS, time e IPC de un proceso existente:

`nsenter --target {{pid}} --uts --time --ipc -- {{comando}} {{argumentos_del_comando}}`

- Ejecuta un comando específico en el espacio de nombres de un proceso existente haciendo referencia a procfs:

`nsenter --pid=/proc/{{pid}}/pid/net -- {{comando}} {{argumentos_del_comando}}`

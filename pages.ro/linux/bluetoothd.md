# bluetoothd

> Daemon pentru gestionarea dispozitivelor bluetooth.
> Mai multe informaţii: <https://manned.org/bluetoothd>

- Porneşte demonul:

`bluetoothd`

- Porniți daemonul, logare la stdout:

`bluetoothd --nodetach`

- Porniți daemonul cu un fișier de configurare specific (implicit la `/etc/bluetooth/main.conf`):

`bluetoothd --configfile {{path/to/file}}`

- Porniți daemonul cu ieșire verbose la stderr:

`bluetoothd --debug`

- Porniți daemonul cu ieșire verbose provenind din anumite fișiere din sursa bluetoothd sau plugin-uri:

`bluetoothd --debug={{path/to/file1}}:{{path/to/file2}}:{{path/to/file3}}`

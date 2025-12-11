# bluetoothd

> Daemon per la gestione dei dispositivi Bluetooth.
> Maggiori informazioni: <https://manned.org/bluetoothd>.

- Avvia il daemon:

`bluetoothd`

- Avvia il daemon, registrando su `stdout`:

`bluetoothd {{[-n|--nodetach]}}`

- Avvia il daemon con un file di configurazione specifico (predefinito `/etc/bluetooth/main.conf`):

`bluetoothd {{[-f|--configfile]}} {{percorso/del/file}}`

- Avvia il daemon con output verboso su `stderr`:

`bluetoothd {{[-d|--debug]}}`

- Avvia il daemon con output verboso proveniente da file specifici in bluetoothd o plugin:

`bluetoothd {{[-d|--debug=]}}{{percorso/del/file1:percorso/del/file2:...}}`

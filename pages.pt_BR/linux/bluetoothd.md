# bluetoothd

> Daemon para gerenciar dispositivos Bluetooth.
> Mais informações: <https://manned.org/bluetoothd>.

- Inicia o daemon:

`bluetoothd`

- Inicia o daemon, registrando em `stdout`:

`bluetoothd {{[-n|--nodetach]}}`

- Inicia o daemon com um arquivo de configuração específico (`/etc/bluetooth/main.conf` por padrão):

`bluetoothd {{[-f|--configfile]}} {{caminho/para/arquivo}}`

- Inicia o daemon com saída verbosa em `stderr`:

`bluetoothd {{[-d|--debug]}}`

- Inicia o daemon com saída verbosa proveniente de arquivos específicos na fonte bluetoothd ou plugins:

`bluetoothd {{[-d|--debug=]}}{{caminho/para/arquivo1:caminho/para/arquivo2:...}}`

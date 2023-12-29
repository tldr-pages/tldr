# bluetoothd

> Daemon para gerenciar dispositivos Bluetooth.
> Mais informações: <https://manned.org/bluetoothd>.

- Inicia o daemon:

`bluetoothd`

- Inicia o daemon, registrando em `stdout`:

`bluetoothd --nodetach`

- Inicia o daemon com um arquivo de configuração específico (`/etc/bluetooth/main.conf` por padrão):

`bluetoothd --configfile {{caminho/para/arquivo}}`

- Inicia o daemon com saída verbosa em `stderr`:

`bluetoothd --debug`

- Inicia o daemon com saída verbosa proveniente de arquivos específicos na fonte bluetoothd ou plugins:

`bluetoothd --debug={{caminho/para/arquivo1}}:{{caminho/para/arquivo2}}:{{caminho/para/arquivo3}}`

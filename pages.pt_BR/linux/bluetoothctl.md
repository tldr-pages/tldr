# bluetoothctl

> Gerencia dispositivos Bluetooth a partir da linha de comando.
> Mais informações: <https://bitbucket.org/serkanp/bluetoothctl>.

- Inicia o shell `bluetoothctl`:

`bluetoothctl`

- Lista todos os dispositivos conhecidos:

`bluetoothctl devices`

- Liga ou desliga o controlador Bluetooth:

`bluetoothctl power {{on|off}}`

- Emparelha com um dispositivo:

`bluetoothctl pair {{endereço_mac}}`

- Remove um dispositivo:

`bluetoothctl remove {{endereço_mac}}`

- Conecta a um dispositivo pareado:

`bluetoothctl connect {{endereço_mac}}`

- Desconecta um dispositivo pareado:

`bluetoothctl disconnect {{endereço_mac}}`

- Exibe ajuda:

`bluetoothctl help`

# az network

> Administrar los recursos de red de Azure.
> Parte de `azure-cli` (también conocido como `az`).
> Más información: <https://learn.microsoft.com/cli/azure/network>.

- Lista los recursos de red en una región que cuenta con una cuota de suscripción:

`az network list-usages`

- Lista todas las redes virtuales en una suscripción:

`az network vnet list`

- Crea una red virtual:

`az network vnet create --address-prefixes {{10.0.0.0/16}} {{[-n|--name]}} {{red_virtual}} {{[-g|--resource-group]}} {{nombre_del_grupo}} --subnet-name {{subred}} --subnet-prefixes {{10.0.0.0/24}}`

- Habilita la red acelerada para una tarjeta de interfaz de red:

`az network nic update --accelerated-networking true {{[-n|--name]}} {{nic}} {{[-g|--resource-group]}} {{grupo_de_recursos}}`

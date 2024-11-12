# octez-client

> Interactúa con la blockchain de Tezos.
> Más información: <https://tezos.gitlab.io/introduction/howtouse.html#client>.

- Configura el cliente con una conexión a un nodo RPC de Tezos como <https://rpc.ghostnet.teztnets.com>:

`octez-client -E {{endpoint}} config update`

- Crea una cuenta y le asigna un alias local:

`octez-client gen keys {{alias}}`

- Obtén el saldo de una cuenta por alias o dirección:

`octez-client get balance for {{alias_o_dirección}}`

- Transfiere tez a otra cuenta:

`octez-client transfer {{5}} from {{alias|address}} to {{alias|address}}`

- Crea (despliega) un contrato inteligente, le asignar un alias local y establece su almacenamiento inicial como un valor codificado por Michelson:

`octez-client originate contract {{alias}} transferring {{0}} from {{alias|address}} running {{ruta/a/archivo_de_origen.tz}} --init "{{almacenamiento_inicial}}" --burn_cap {{1}}`

- Llama a un contrato inteligente por su alias o dirección y pasa un parámetro codificado por Michelson:

`octez-client transfer {{0}} from {{alias|address}} to {{contract}} --entrypoint "{{entrypoint}}" --arg "{{parámetro}}" --burn-cap {{1}}`

- Muestra ayuda:

`octez-client man`

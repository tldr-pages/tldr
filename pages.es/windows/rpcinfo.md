# rpcinfo

> Lista programas vía RPC en computadoras remotas.
> Más información: <https://learn.microsoft.com/windows-server/administration/windows-commands/rpcinfo>.

- Listar todos los programas registrados en la computadora local:

`rpcinfo`

- Listar todos los programas registrados en una computadora remota:

`rpcinfo /p {{nombre_de_computadora}}`

- Llamar a un programa específico en una computadora remota usando TCP:

`rpcinfo /t {{nombre_de_computadora}} {{nombre_del_programa}}`

- Llamar a un programa específico en una computadora remota usando UDP:

`rpcinfo /u {{nombre_de_computadora}} {{nombre_del_programa}}`

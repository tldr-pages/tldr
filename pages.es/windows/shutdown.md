# shutdown

> Una herramienta para apagar, reiniciar o cerrar sesión en una máquina.
> Más información: <https://learn.microsoft.com/windows-server/administration/windows-commands/shutdown>.

- Apagar la máquina actual:

`shutdown /s`

- Apagar la máquina actual forzando el cierre de todas las aplicaciones:

`shutdown /s /f`

- Reiniciar la máquina actual inmediatamente:

`shutdown /r /t 0`

- Hibernar la máquina actual:

`shutdown /h`

- Cerrar sesión en la máquina actual:

`shutdown /l`

- Especificar un tiempo de espera en segundos antes de apagar:

`shutdown /s /t {{8}}`

- Abortan una secuencia de apagado cuyo tiempo de espera aún no ha expirado:

`shutdown /a`

- Apagar una máquina remota:

`shutdown /m {{\\hostname}}`

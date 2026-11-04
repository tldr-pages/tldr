# shutdown

> Una herramienta para apagar, reiniciar o cerrar sesión en una máquina.
> Más información: <https://learn.microsoft.com/windows-server/administration/windows-commands/shutdown>.

- Apaga la máquina actual:

`shutdown /s`

- Apaga la máquina actual forzando el cierre de todas las aplicaciones:

`shutdown /s /f`

- Reinicia la máquina actual inmediatamente:

`shutdown /r /t 0`

- Hiberna la máquina actual:

`shutdown /h`

- Cierra sesión en la máquina actual:

`shutdown /l`

- Especifica un tiempo de espera en segundos antes de apagar:

`shutdown /s /t {{8}}`

- Aborta una secuencia de apagado cuyo tiempo de espera aún no ha expirado:

`shutdown /a`

- Apaga una máquina remota:

`shutdown /m {{\\hostname}}`

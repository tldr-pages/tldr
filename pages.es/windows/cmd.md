# cmd

> El intérprete de comandos de Windows.
> Más información: <https://learn.microsoft.com/windows-server/administration/windows-commands/cmd>.

- Iniciar una sesión shell interactiva:

`cmd`

- Ejecutar [c]omandos específicos:

`cmd /c {{echo Hola Mundo}}`

- Ejecutar un script específico:

`cmd {{ruta\al\script.bat}}`

- Ejecutar comandos específicos y luego entrar en un shell interactivo:

`cmd /k {{echo Hola Mundo}}`

- Iniciar una sesión shell interactiva donde `echo` está desactivado en la salida de comandos:

`cmd /q`

- Iniciar una sesión shell interactiva con la expansión [v]ariable retardada activada o desactivada:

`cmd /v:{{on|off}}`

- Iniciar una sesión shell interactiva con [e]xtensiones de comando activadas o desactivadas:

`cmd /e:{{on|off}}`

- Iniciar una sesión shell interactiva with con la codificación [u]nicode utilizada:

`cmd /u`

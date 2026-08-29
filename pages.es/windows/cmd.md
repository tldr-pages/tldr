# cmd

> El intérprete de comandos de Windows.
> Más información: <https://learn.microsoft.com/windows-server/administration/windows-commands/cmd>.

- Inicia una sesión shell interactiva:

`cmd`

- Ejecuta [c]omandos específicos:

`cmd /c {{echo cmd es ejecutado}}`

- Ejecuta un script específico:

`cmd {{ruta\al\script.bat}}`

- Ejecuta comandos específicos y luego entrar en un shell interactivo:

`cmd /k {{echo 'cmd es ejecutado'}}`

- Inicia una sesión shell interactiva donde `echo` está desactivado en la salida de comandos:

`cmd /q`

- Inicia una sesión shell interactiva con la expansión [v]ariable retardada activada o desactivada:

`cmd /v:{{on|off}}`

- Inicia una sesión shell interactiva con [e]xtensiones de comando activadas o desactivadas:

`cmd /e:{{on|off}}`

- Inicia una sesión shell interactiva with con la codificación [u]nicode utilizada:

`cmd /u`

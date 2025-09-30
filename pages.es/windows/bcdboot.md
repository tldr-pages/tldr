# bcdboot

> Configura o repara archivos de arranque.
> Más información: <https://learn.microsoft.com/windows-hardware/manufacture/desktop/bcdboot-command-line-options-techref-di>.

- Inicializa la partición del sistema utilizando archivos BCD de la carpeta de Windows de origen:

`bcdboot {{C:\Windows}}`

- Habilita el modo [v]erboso:

`bcdboot {{C:\Windows}} /v`

- Especificar la letra de volumen de la partición [s]istema:

`bcdboot {{C:\Windows}} /s {{S:}}`

- Especifica un idioma [l]ocal:

`bcdboot {{C:\Windows}} /l {{es-es}}`

- Especifica un tipo de [f]irmware al copiar los archivos de arranque a un volumen especificado:

`bcdboot {{C:\Windows}} /s {{S:}} /f {{UEFI|BIOS|ALL}}`

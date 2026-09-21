# fondue

> Instala características opcionales de Windows.
> Más información: <https://learn.microsoft.com/windows-server/administration/windows-commands/fondue>.

- Habilita una característica específica de Windows:

`fondue /enable-feature:{{característica}}`

- Ocultar todos los mensajes de salida al usuario:

`fondue /enable-feature:{{característica}} /hide-ux:all`

- Especifica un nombre de proceso llamador para la información de errores:

`fondue /enable-feature:{{característica}} /caller-name:{{nombre}}`

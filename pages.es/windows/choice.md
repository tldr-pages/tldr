# choice

> Solicita al usuario que seleccione una opción y devuelve el índice de la opción seleccionada.
> Más información: <https://learn.microsoft.com/windows-server/administration/windows-commands/choice>.

- Solicita al usuario actual que seleccione una opción `Y` o `N`:

`choice`

- Solicita al usuario actual que seleccione una op[c]ión de un conjunto específico:

`choice /c {{AB}}`

- Solicita al usuario actual que seleccione una opción con un [m]ensaje específico:

`choice /m "{{mensaje}}"`

- Solicita al usuario actual que seleccione una opción Mayús[c]ula-[s]ensible de un conjunto específico:

`choice /cs /c {{Ab}}`

- Solicita al usuario actual que seleccione una opción y preferir la opción pre[d]eterminada en un [t]iempo específico:

`choice /t {{5}} /d {{opcion_predeterminada}}`

- Muestra la ayuda:

`choice /?`

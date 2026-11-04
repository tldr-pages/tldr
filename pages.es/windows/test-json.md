# Test-Json

> Verifica si una cadena es un documento JSON válido.
> Nota: Este comando solo se puede usar en PowerShell.
> Más información: <https://learn.microsoft.com/powershell/module/microsoft.powershell.utility/test-json>.

- Verifica si una cadena desde `stdin` está en formato JSON:

`'{{cadena}}' | Test-Json`

- Verifica si una cadena está en formato JSON:

`Test-Json -Json '{{json_a_verificar}}'`

- Verifica si una cadena desde `stdin` cumple con un esquema JSON específico:

`'{{cadena}}' | Test-Json -SchemaFile {{ruta\a\archivo_esquema.json}}`

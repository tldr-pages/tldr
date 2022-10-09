# dotnet restore

> Restarua las dependencias y herramientas de un proyecto .NET.
> Más información: <https://learn.microsoft.com/dotnet/core/tools/dotnet-restore>.

- Restaura dependencias para un proyecto o solución .NET en el directorio actual:

`dotnet restore`

- Restaura dependencias para un proyecto o solución .NET en una ubicación específica:

`dotnet restore {{ruta/al/proyecto_o_solución}}`

- Restaura depedencias sin almacenar las solicitudes HTTP en caché:

`dotnet restore --no-cache`

- Obliga a todas las dependencias a ser resueltas incluso si la última restauración fue exitosa:

`dotnet restore --force`

- Restaura dependencias usando los orígenes con error como advertencias:

`dotnet restore --ignore-failed-sources`

- Restaura dependencias con un nivel específico de verbosidad:

`dotnet restore --verbosity {{quiet|minimal|normal|detailed|diagnostic}}`

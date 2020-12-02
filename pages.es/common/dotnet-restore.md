# dotnet restore

> Restarua las dependencias y herramientas de un proyecto .NET.
> Más información: https://docs.microsoft.com/dotnet/core/tools/dotnet-restore.

- Restaura dependencias para un proyecto o solución .NET en el directorio actual:

`dotnet restore`

- Restaura dependencias para un proyecto o solución .NET en una ubicación específica:

`dotnet restore {{ruta/al/proyecto_o_solución}}

- Restaura depedencias sin tomar las solicitudes HTTP:

`dotnet restore --no-cache

- Obliga a todas las dependencias a ser resueltas incluso si la última restauración fue exitosa:

`dotnet restore --force`

- Restaura dependencias usando las fallas del paquete fuente como advertencias:

`dotnet restore --ignore-failed-sources`

- Restaura dependencias con un nivel específico de verbosidad:

`dotnet restore --verbosity {{el|mínimo|normal|diagnóstico|detallado}}
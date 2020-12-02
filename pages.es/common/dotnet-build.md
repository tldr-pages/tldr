# dotnet build

>Construye una aplicación .NET y sus dependencias. Más información en: https://docs.microsoft.com/dotnet/core/tools/dotnet-build

- Compila el proyecto o solución en el directorio actual:

`dotnet build`

- Compila un proyecto o solución .NET en el modo de depuración:

`dotnet build {{ruta/al/proyecto_o_solucion}}`

- Compila en modo de lanzamiento:

`dotnet build --configuration {{Lanzamiento}}`

- Compila sin restaurar las dependencias:

`dotnet build --no-restore`

- Compila con un nivel específico de verbosidad:

`dotnet build --verbosity {{el|mínimo|diagnóstico|normal|detallado}}`

- Compila para un tiempo de ejecución específico:

`dotnet build --runtime {{identificador_del_tiempo_de_ejecución}}`

- Especifica el directorio de salida:

`dotnet build --output {{ruta/al/directorio}}`
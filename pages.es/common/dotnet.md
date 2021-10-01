# dotnet

> Herramienta multiplataforma de línea de comandos para .NET Core.
> Algunos subcomandos, como `dotnet build`, tienen su propia documentación de uso.
> Más información: <https://docs.microsoft.com/dotnet/core/tools>.

- Inicializa un proyecto .NET nuevo:

`dotnet new {{nombre_de_la_plantilla}}`

- Restaura los paquetes NuGet:

`dotnet restore`

- Compila y ejectura el proyecto .NET en el directorio actual:

`dotnet run`

- Ejecuta una aplicación dotnet empaquetada (solo necesita el entorno en tiempo de ejecución, el resto de los comandos requieren el SDK de .NET Core instalado):

`dotnet {{ruta/a/la/aplicación.dll}}`

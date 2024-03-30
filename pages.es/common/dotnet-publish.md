# dotnet publish

> Publica una aplicación .NET y sus dependencias en una carpeta para la implementación en un sistema de hospedaje.
> Más información: <https://learn.microsoft.com/dotnet/core/tools/dotnet-publish>.

- Compila un proyecto .NET en modo de lanzamiento:

`dotnet publish --configuration Release {{ruta/al/archivo_del_proyecto}}`

- Publica el entorno de ejecución de .NET Core con la aplicación para un entorno de ejecución específico:

`dotnet publish --self-contained true --runtime {{identificador_del_entorno_en_tiempo_de_ejecución}} {{ruta/al/archivo_del_proyecto}}`

- Empaqueta la aplicación en un archivo ejecutable único de una plataforma específica:

`dotnet publish --runtime {{identificador_del_entorno_en_tiempo_de_ejecucución}} -p:PublishSingleFile=true {{ruta/al/archivo_del_proyecto}}`

- Recorta las bibliotecas no usadas para reducir el tamaño de la aplicación:

`dotnet publish --self-contained true --runtime {{identificador_del_entorno_de_tiempo_de_ejecución}} -p:PublishTrimmed=true {{ruta/al/archivo_del_proyecto}}`

- Compila un proyecto .NET sin restaurar las dependencias:

`dotnet publish --no-restore {{ruta/al/archivo_del_proyecto}}`

- Especifica el directorio de salida:

`dotnet publish --output {{ruta/al/directorio}} {{ruta/al/archivo_del_proyecto}}`

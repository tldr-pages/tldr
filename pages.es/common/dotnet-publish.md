# dotnet publish

> Publica una aplicación .NET y sus dependencias en una carpeta para despliegue de un sistema local.
> Más información: https://docs.microsoft.com/dotnet/core/tools/dotnet-publish.

- Compila un proyecto .NET en modo de lanzamiento:

`dotnet publish --configuration Release {{ruta/al/archivo_del_proyecto}}`

- Publica el tiempo de ejecución de .NET Core con la aplicación para el tiempo de ejecución especificado:

`dotnet publish --self-contained true --runtime {{identificador_del_tiempo_de_ejecución}} {{ruta/al/archivo_del_proyecto}}`

- Empaqueta la aplicación en un archivo ejecutable unico de una plataforma específica:

`dotnet publish --runtime {{identificador_del_tiempo_de_ejecucución}} -p:PublishSingleFile=true {{ruta/al/archivo_del_proyecto}}`

- Recorta librerías no usadas para reducir el tamaño de la aplicación desplegada:

`dotnet publish --self-contained true --runtime {{identificador_del_tiempo_de_ejecución}} -p:PublishTrimmed=true {{ruta/al/archivo_del_proyecto}}`

- Compila un proyecto .NET sin restaurar las dependencias:

`dotnet publish --no-restore {{ruta/al/archivo_del_proyecto}}`

- Especifica el directorio de salida:

`dotnet publish --output {{ruta/al/directorio}} {{ruta/al/archivo_del_proyecto}}`

# dotnet publish

> Publica una aplicación .NET y sus dependencias en una carpeta para despliegue de un sistema local.
> Más información: https://docs.microsoft.com/dotnet/core/tools/dotnet-publish.

- Complisa un proyecto .NET en el modo de lanzamiento:

`dotnet publish --configuration Release {{ruta/al/archivo_del_proyecto}}`

- Publica el tiempo de ejecución de .NET Core con tu aplicación para el tiempo de ejecución especificado:

`dotnet publish --self-contained true --runtime {{identificador_del_tiempo_de_ejecución}}`

- Empaqueta la aplicación en un único-archivo ejecutable de una plataforma-específica:

`dotnet publish --runtime {{identificador_del_tiempo_de_ejecucución}} -p:PublishSingleFile=true {{ruta/al/archivo_del_proyecto}}`

- Recorta librerías no usadas para reducir el tamaño del despliegue de una aplicación:

`dotnet publish --self-contained true --runtime {{identificador_del_tiempo_de_ejecución}} -p:PublishTrimmed=true {{ruta/al/archivo_del_proyecto}}`

- Compila un proyecto .NET sin restaurar las dependencias:

`dotnet publish --no-restore {{ruta/al/archivo_del_proyecto}}`

- Especifica el directorio de salida:

`dotnet publish --output {{ruta/al/directorio}} {{ruta/al/archivo_del_proyecto}}`
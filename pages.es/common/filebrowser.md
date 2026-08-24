# filebrowser

> Sencillo servidor web HTTP para gestionar archivos y directorios.
> Más información: <https://filebrowser.org/cli/filebrowser.html>.

- Inicia una nueva instancia del servidor sirviendo el directorio actual:

`filebrowser`

- Inicia una nueva instancia de servidor sirviendo un directorio raíz específico:

`filebrowser {{[-r|--root]}} {{ruta/al/directorio}}`

- Inicia una instancia con una dirección de host (por defecto `127.0.0.1`) y un puerto (por defecto `8080`) diferentes:

`filebrowser {{[-a|--address]}} {{host}} {{[-p|--port]}} {{puerto}} {{[-r|--root]}} {{ruta/al/directorio}}`

- Inicia una instancia con un archivo de configuración especificado, almacenando la base de datos de la aplicación en una ubicación específica (por defecto es `filebrowser.db` en el directorio actual):

`filebrowser {{[-c|--config]}} {{ruta/al/archivo}} {{[-d|--database]}} {{ruta/a/base_de_datos.db}} {{[-r|--root]}} {{ruta/al/directorio}}`

- Configura un nombre de usuario y una contraseña diferentes para la primera cuenta (ambos por defecto `admin`) cuando configure una nueva instancia:

`filebrowser --username {{nombre_de_usuario}} --password {{contraseña}} {{[-r|--root]}} {{ruta/al/directorio}}`

- Configura la cantidad máxima de procesadores de imágenes utilizados al generar miniaturas (por defecto es `4`):

`filebrowser --img-processors {{4}} {{[-r|--root]}} {{ruta/al/directorio}}`

- Desactiva las miniaturas de imágenes, así como la función Command Runner, que limita el acceso a los archivos de secuencia de comandos alojados para que no se ejecuten dentro de la aplicación:

`filebrowser --disable-exec --disable-thumbnails {{[-r|--root]}} {{ruta/al/directorio}}`

- Deshabilita el cambio de tamaño de las vistas previas de imágenes, así como la detección de tipos de archivo mediante la lectura de sus cabeceras:

`filebrowser --disable-preview-resize --disable-type-detection-by-header {{[-r|--root]}} {{ruta/al/directorio}}`

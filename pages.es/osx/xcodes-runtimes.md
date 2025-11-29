# xcodes runtimes

> Gestiona los tiempos de ejecución de Xcode Simulator.
> Más información: <https://github.com/xcodesorg/xcodes#commands>.

- Muestra todos los tiempos de ejecución del simulador disponibles:

`xcodes runtimes --include-betas`

- Descarga un tiempo de ejecución para el Simulator:

`xcodes runtimes download {{nombre_del_tiempo_de_ejecución}}`

- Descarga e instala un tiempo de ejecución para el Simulator:

`xcodes runtimes install {{nombre_del_tiempo_de_ejecución}}`

- Descarga/instala un tiempo de ejecución del Simulator para una versión específica de iOS/watchOS/tvOS/visionOS (debe escribirse distinguiendo entre mayúsculas y minúsculas):

`xcodes runtimes {{download|install}} "{{iOS|watchOS|tvOS|visionOS}} {{versión_de_tiempo_de_ejecución}}"`

- Establece una ubicación específica en la que se descargará primero el archivo de tiempo de ejecución (por defecto es `~/Downloads`):

`xcodes runtimes {{download|install}} {{nombre_del_tiempo_de_ejecución}} --directory {{ruta/a/directorio}}`

- No elimina el archivo descargado cuando el Simulator se instala correctamente:

`xcodes runtimes install {{nombre_del_tiempo_de_ejecución}} --keep-archive`

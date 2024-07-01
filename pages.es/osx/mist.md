# mist

> MIST - macOS Installer Super Tool.
> Descarga automáticamente Firmwares/Instaladores de macOS.
> Más información: <https://github.com/ninxsoft/mist-cli>.

- Lista todos los firmwares de macOS disponibles para los Mac Silicon de Apple:

`mist list firmware`

- Lista todos los instaladores de macOS disponibles para Mac Intel, incluidos los instaladores universales para macOS Big Sur y versiones posteriores:

`mist list installer`

- Lista todos los instaladores de macOS compatibles con esta Mac, incluidos los instaladores universales de macOS Big Sur y posteriores:

`mist list installer --compatible`

- Lista todos los instaladores de macOS disponibles para Mac Intel, incluidas las betas tanto como también los instaladores universales para macOS Big Sur y versiones posteriores:

`mist list installer --include-betas`

- Lista solo el último instalador de macOS Sonoma para las Macs Intel, incluidos los instaladores universales de macOS Big Sur y posteriores:

`mist list installer --latest "macOS Sonoma"`

- Lista y exporta instaladores de macOS a un archivo CSV:

`mist list installer --export "{{/ruta/a/archivo_con_datos_exportados.csv}}"`

- Descarga el último firmware de macOS Sonoma para los Mac Silicon de Apple, con un nombre personalizado:

`mist download firmware "macOS Sonoma" --firmware-name "{{Install %NAME% %VERSION%-%BUILD%.ipsw}}"`

- Descarga una versión específica del instalador de macOS para Mac Intel, incluidos los instaladores universales de macOS Big Sur y posteriores:

`mist download installer "{{13.5.2}}" application`

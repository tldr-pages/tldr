# osascript

> Ejecuta AppleScript o JavaScript for Automation (JXA) desde la línea de comandos.
> Más información: <https://ss64.com/osx/osascript.html>.

- Ejecuta un comando AppleScript:

`osascript -e "{{say 'Hello world'}}"`

- Ejecuta varios comandos AppleScript:

`osascript -e "{{say 'Hello'}}" -e "{{say 'world'}}"`

- Ejecuta un archivo AppleScript compilado (`*.scpt`), empaquetado (`*.scptd`) o un archivo Applescript en texto plano (`*.applescript`):

`osascript {{ruta/al/apple.scpt}}`

- Obtén el identificador del paquete de una aplicación (útil para `open -b`):

`osascript -e 'id of app "{{Application}}"'`

- Ejecuta un comando JavaScript:

`osascript -l JavaScript -e "{{console.log('Hola mundo');}}"`

- Ejecuta un archivo JavaScript:

`osascript -l JavaScript {{ruta/al/script.js}}`

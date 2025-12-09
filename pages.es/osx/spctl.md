# spctl

> Gestiona el subsistema de políticas de evaluación de seguridad.
> Utilidad para gestionar Gatekeeper en macOS.
> Más información: <https://keith.github.io/xcode-man-pages/spctl.8.html>.

- Desactiva Gatekeeper:

`spctl --master-disable`

- Añade una regla para permitir la ejecución de una aplicación (el etiquetado de la regla es opcional):

`spctl --add --label {{nombre_regla}} {{ruta/al/archivo}}`

- Activa Gatekeeper:

`spctl --master-enable`

- Lista todas las reglas del sistema:

`spctl --list`

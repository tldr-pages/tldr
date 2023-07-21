# spctl

> Gestiona el subsistema de políticas de evaluación de seguridad.
> Utilidad para gestionar Gatekeeper en macOS.
> Más información: <https://www.unix.com/man-page/osx/8/SPCTL/>.

- Desactiva Gatekeeper:

`spctl --master-disable`

- Añade una regla para permitir la ejecución de una aplicación (el etiquetado de la regla es opcional):

`spctl --add --label {{nombre_regla}} {{ruta/al/archivo}}`

- Activa Gatekeeper:

`spctl --master-enable`

- Lista todas las reglas del sistema:

`spctl --list`

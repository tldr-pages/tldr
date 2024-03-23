# tmutil

> Utilidad para gestionar las copias de seguridad de Time Machine. La mayoría de las acciones requieren privilegios de root.
> Más información: <https://keith.github.io/xcode-man-pages/tmutil.8.html>.

- Establece una unidad HFS+ como destino de la copia de seguridad:

`sudo tmutil setdestination {{ruta/al/punto_montaje_disco}}`

- Establece un recurso compartido APF o SMB como destino de la copia de seguridad:

`sudo tmutil setdestination "{{protocolo://usuario[:contraseña]@host/compartir}}"`

- Añade el destino indicado a la lista de destinos:

`sudo tmutil setdestination -a {{destino}}`

- Activa copias de seguridad automáticas:

`sudo tmutil enable`

- Desactiva las copias de seguridad automáticas:

`sudo tmutil disable`

- Inicia una copia de seguridad, si ya no se está ejecutando, y libera el control del intérprete de comandos:

`sudo tmutil startbackup`

- Inicia una copia de seguridad y bloquearla hasta que termine:

`sudo tmutil startbackup -b`

- Detiene una copia de seguridad:

`sudo tmutil stopbackup`

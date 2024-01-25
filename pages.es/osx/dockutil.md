# dockutil

> Gestiona los elementos del dock de macOS.
> Más información: <https://github.com/kcrawford/dockutil>.

- Añade una aplicación al final del dock del usuario actual:

`dockutil --add {{ruta/a/la/aplicación}}`

- Reemplaza una aplicación por otra en el dock del usuario actual:

`dockutil --add {{ruta/a/la/aplicación}} --replacing '{{etiqueta_de_elemento_del_dock}}'`

- Añade un directorio con opciones de visualización y lo muestra como un icono de carpeta o pila:

`dockutil --add {{/ruta/al/directorio}} --view {{grill|fan|list|auto}} --display {{folder|stack}}`

- Añade la URL de un elemento del dock después de otro elemento:

`dockutil --add {{vnc://ejemplo_servidor.local}} --label '{{VNC de ejemplo}}' --after {{etiqueta_de_elemento_del_dock}}`

- Elimina una aplicación del dock dado su nombre de etiqueta en el dock:

`dockutil --remove '{{etiqueta_de_elemento_del_dock}}'`

- Añade un espaciador en una sección después de una aplicación:

`dockutil --add '' --type {{spacer|small-spacer|flex-spacer}} --section {{apps}} --after {{etiqueta_de_elemento_del_dock}}`

- Elimina todos los elementos espaciadores:

`dockutil --remove spacer-tiles`

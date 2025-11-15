# deborphan

> Muestra paquetes huérfanos en sistemas operativos usando el administrador de paquetes APT.
> Más información: <https://manned.org/deborphan>.

- Muestra paquetes de biblioteca (de la sección "libs" del repositorio de paquetes) que no son requeridos por otro paquete:

`deborphan`

- Lista paquetes huérfanos de la sección "libs", así como paquetes huérfanos que tienen un nombre que parece un nombre de biblioteca:

`deborphan --guess-all`

- Busca paquetes que son recomendados o sugeridos (pero no requeridos) por otro paquete:

`deborphan --nice-mode`

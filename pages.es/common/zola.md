# zola

> Un generador de sitios estáticos en un único binario con todo incorporado.
> Más información: <https://www.getzola.org/documentation/getting-started/cli-usage/>.

- Crea la estructura de directorios utilizada por Zola en el directorio dado:

`zola init {{mi_sitio}}`

- Construye todo el sitio en el directorio `public` después de eliminarlo:

`zola build`

- Construye todo el sitio en un directorio diferente:

`zola build --output-dir {{ruta/al/directorio_resultado/}}`

- Construye y sirve el sitio usando un servidor local (por defecto es `127.0.0.1:1111`):

`zola serve`

- Construye todas las páginas como lo haría el comando build, pero sin escribir ninguno de los resultados al disco:

`zola check`

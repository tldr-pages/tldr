# ccache

> Caché del compilador C/C++.
> Nota: los paquetes suelen proporcionar enlaces simbólicos para los compiladores en `/usr/lib/ccache/bin`. Anteponga este directorio en `$PATH` para utilizar automáticamente `ccache` con los compiladores.
> Más información: <https://ccache.dev/manual/latest.html>.

- Muestra las e[s]tadísticas de la caché actual:

`ccache {{[-s|--show-stats]}}`

- Borra toda la caché:

`ccache {{[-C|--clear]}}`

- Restablece ([z]ero) las estadísticas (pero no la propia caché):

`ccache {{[-z|--zero-stats]}}`

- Compila código C y almacena la salida compilada en la caché (para usar `ccache` en todas las invocaciones de `gcc`, lea la nota anterior):

`ccache gcc {{ruta/al/archivo.c}}`

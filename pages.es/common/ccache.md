# ccache

> Caché del compilador C/C++.
> Nota: los paquetes suelen proporcionar enlaces simbólicos para los compiladores en `/usr/lib/ccache/bin`. Anteponga este directorio a `$PATH` para utilizar automáticamente `ccache` para los mismos.
> Más información: <https://ccache.dev/manual/latest.html>.

- Muestra las e[s]tadísticas de la caché actual:

`ccache --show-stats`

- Borra toda la caché:

`ccache --clear`

- Restablece ([z]ero) las estadísticas (pero no la propia caché):

`ccache --zero-stats`

- Compila código C y cachea la salida compilada (para usar `ccache` en todas las invocaciones `gcc`, lea la nota anterior):

`ccache gcc {{ruta/al/archivo.c}}`

# zig

> El compilador Zig y la cadena de herramientas.
> Más información: <https://ziglang.org/documentation/master/>.

- Compila el proyecto en el directorio actual:

`zig build`

- Compila y ejecuta el proyecto en el directorio actual:

`zig build run`

- Inicializa un proyecto `zig build` con biblioteca y ejecutable:

`zig init`

- Crea y ejecuta una compilación de pruebas:

`zig test {{ruta/al/archivo.zig}}`

- Hace compilación cruzada, arma y ejecuta un proyecto para la arquitectura `x86_64` y el sistema operativo `windows`:

`zig build run -fwine -Dtarget=x86_64-windows`

- Reformatea código fuente Zig en forma canónica:

`zig fmt {{ruta/al/archivo.zig}}`

- Traduce un archivo C a `zig`:

`zig translate-c -lc {{ruta/al/archivo.c}}`

- Usa Zig como compilador de C++:

`zig c++ {{ruta/al/archivo.cpp}}`

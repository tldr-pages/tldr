# abrt-action-analyze-backtrace

> Analiza un backtrace de C/C++.
> Genera un hash de duplicación, una clasificación del backtrace e identifica la función que causó el fallo.
> Guarda los datos como nuevos elementos `duphash`, `rating`, `crash_function` en el directorio del problema.
> Más información: <https://manned.org/abrt-action-analyze-backtrace>.

- Analiza el backtrace para el directorio de trabajo actual:

`abrt-action-analyze-backtrace`

- Analiza el backtrace para un directorio específico:

`abrt-action-analyze-backtrace -d {{ruta/al/directorio}}`

- Analiza el backtrace de manera detallada:

`abrt-action-analyze-backtrace -v`

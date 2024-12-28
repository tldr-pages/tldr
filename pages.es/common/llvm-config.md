# llvm-config

> Obtiene variada información de configuración necesaria para compilar programas que utilizan LLVM.
> Típicamente llamado desde sistemas de construcción, como Makefiles o scripts de configuración.
> Más información: <https://llvm.org/docs/CommandGuide/llvm-config.html>.

- Compila y vincula un programa basado en LLVM:

`clang++ $(llvm-config --cxxflags --ldflags --libs) --output {{ruta/al/resultado_ejecutable}} {{ruta/a/source.cc}}`

- Imprime el `PREFIJO` de su instalación LLVM:

`llvm-config --prefix`

- Imprime todos los objetivos soportados por su LLVM instalado:

`llvm-config --targets-built`

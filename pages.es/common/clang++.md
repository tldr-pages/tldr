# clang++

> Compila archivos con código fuente C++.
> Hace parte de LLVM.
> Más información: <https://clang.llvm.org>.

- Compila un conjunto de archivos de código fuente a un binario ejecutable:

`clang++ {{ruta/al/código1.cpp ruta/al/código2.cpp ...}} {{[-o|--output]}} {{ruta/al/ejecutable}}`

- Activa la visualización de todos los errores y advertencias:

`clang++ {{ruta/al/código.cpp}} -Wall {{[-o|--output]}} {{ruta/al/ejecutable}}`

- Muestra advertencias comunes, símbolos de depuración en la salida y optimiza sin afectar la depuración:

`clang++ {{ruta/al/código.cpp}} -Wall {{[-g|--debug]}} -Og {{[-o|--output]}} {{ruta/al/ejecutable}}`

- Elije un estándar de lenguaje para compilar:

`clang++ {{ruta/al/código.cpp}} -std={{c++20}} {{[-o|--output]}} {{ruta/al/ejecutable}}`

- Incluye las bibliotecas ubicadas en una ruta distinta a la del código fuente:

`clang++ {{ruta/al/código.cpp}} {{[-o|--output]}} {{ruta/al/ejecutable}} -I{{ruta/al/directorio/de/headers}} -L{{ruta/al/directorio/de/bibliotecas}} -l{{ruta/a/la/biblioteca}}`

- Compila el código fuente hacia una representación intermedia (IR) LLVM:

`clang++ {{[-S|--assemble]}} -emit-llvm {{ruta/al/código.cpp}} {{[-o|--output]}} {{ruta/a/la/representación.ll}}`

- Optimiza el programa compilado en función de la velocidad:

`clang++ {{ruta/al/código.cpp}} -O{{1|2|3|fast}} {{[-o|--output]}} {{ruta/al/ejecutable}}`

- Muestra la versión:

`clang++ --version`

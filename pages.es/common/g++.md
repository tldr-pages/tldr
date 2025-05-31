# g++

> Preprocesa y compila archivos de código fuente de C++.
> Parte de GCC (GNU Compiler Collection).
> Más información: <https://gcc.gnu.org>.

- Compila varios archivo de código fuente en un ejecutable:

`g++ {{ruta/al/código_fuente1.cpp ruta/al/código_fuente2.cpp ...}} {{[-o|--output]}} {{ruta/al/ejecutable}}`

- Activa todos los errores y advertencias:

`g++ {{ruta/al/código_fuente.cpp}} -Wall {{[-o|--output]}} {{ejecutable}}`

- Muestra advertencias comunes, añade símbolos de depuración a la salida y optimiza sin afectar la depuración:

`g++ {{ruta/al/código_fuente.cpp}} -Wall {{[-g|--debug]}} -Og {{[-o|--output]}} {{ruta/al/ejecutable}}`

- Elija un lenguaje estándar para compilar (C++98/C++11/C++14/C++17):

`g++ {{ruta/al/código_fuente.cpp}} -std={{c++98|c++11|c++14|c++17}} {{[-o|--output]}} {{ruta/al/ejecutable}}`

- Incluye bibliotecas de una ruta diferente:

`g++ {{ruta/al/código_fuente.cpp}} {{[-o|--output]}} {{ruta/al/ejecutable}} -I{{ruta/al/encabezado}} -L{{ruta/a/la/biblioteca}} -l{{nombre_de_la_biblioteca}}`

- Enlaza y compila múltiples archivos en un ejecutable:

`g++ {{[-c|--compile]}} {{ruta/al/código_fuente1.cpp ruta/al/código_fuente2.cpp ...}} && g++ {{[-o|--output]}} {{ruta/al/ejecutable}} {{ruta/al/código_fuente1.o ruta/al/código_fuente2.o ...}}`

- Optimiza el programa compilado para mejorar la velocidad de ejecución:

`g++ {{ruta/al/código_fuente.cpp}} -O{{1|2|3|fast}} {{[-o|--output]}} {{ruta/al/ejecutable}}`

- Muestra la versión del programa:

`g++ --version`

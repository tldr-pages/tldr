# gcc

> Preprocesa y compila archivos de código fuente C y C++, luego los ensambla y los une.
> Parte de GCC Colección de Compilación GNU (GNU Compiler Collection).
> Más información: <https://gcc.gnu.org/onlinedocs/gcc/>.

- Compila varios archivos de código fuente en un ejecutable:

`gcc {{ruta/a/la/fuente1.c ruta/a/la/fuente2.c ...}} {{[-o|--output]}} {{ruta/al/ejecutable}}`

- Muestra todos los errores y advertencias:

`gcc {{ruta/a/la/fuente.c}} -Wall {{[-o|--output]}} {{ejecutable}}`

- Muestra las advertencias comunes, añade símbolos de depuración en el ejecutable, y optimiza sin afectar la depuración:

`gcc {{ruta/a/la/fuente.c}} -Wall {{-g|--debug}} -Og {{[-o|--output]}} {{ruta/al/ejecutable}}`

- Incluye las bibliotecas de una ruta diferente:

`gcc {{ruta/a/la/fuente.c}} {{[-o|--output]}} {{ruta/al/ejecutable}} -I{{ruta/a/header}} -L{{ruta/a/la/biblioteca}} -l{{nombre_de_biblioteca}}`

- Compila el código fuente a instrucciones de Ensamblador (Assembler):

`gcc {{[-S|--assemble]}} {{ruta/a/la/fuente.c}}`

- Compila el código fuente a un archivo objeto sin vincular:

`gcc {{[-c|--compile]}} {{ruta/a/la/fuente.c}}`

- Optimiza el programa compilado en función de velocidad de ejecución:

`gcc {{ruta/a/la/fuente.c}} -O{{1|2|3|fast}} {{[-o|--output]}} {{ruta/al/ejecutable}}`

- Versión de visualización:

`gcc --version`

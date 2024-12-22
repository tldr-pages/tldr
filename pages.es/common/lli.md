# lli

> Ejecuta directamente programas desde el código de bits LLVM (bitcode).
> Más información: <https://www.llvm.org/docs/CommandGuide/lli.html>.

- Ejecuta un código de bits o un archivo IR:

`lli {{ruta/al/archivo.ll}}`

- Ejecuta con argumentos de línea de comandos:

`lli {{ruta/al/archivo.ll}} {{primer_argumento segundo_argumento ...}}`

- Habilita todas las optimizaciones:

`lli -O3 {{ruta/al/archivo.ll}}`

- Carga una biblioteca dinámica antes de vincular:

`lli --dlopen={{ruta/a/biblioteca.dll}} {{ruta/al/archivo.ll}}`

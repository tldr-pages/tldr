# llc

> Compila Representación intermedia LLVM o código bit (bitcode) para el lenguaje ensamblador objetivo específico.
> Más información: <https://www.llvm.org/docs/CommandGuide/llc.html>.

- Compila un bitcode o archivo IR a un archivo ensamblador con el mismo nombre base:

`llc {{ruta/al/archivo.ll}}`

- Habilita todas las optimizaciones:

`llc -O3 {{ruta/al/archivo.ll}}`

- Dirige la salida a un archivo específico:

`llc --output {{ruta/al/resultado.s}}`

- Emite código, independiente de la posición que pueda reubicarse completamente:

`llc -relocation-model=pic {{ruta/a/la/entrada.ll}}`

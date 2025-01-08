# lit

> Comprobador integrado LLVM para ejecutar conjuntos de pruebas estilo LLVM y Clang, resumiendo los resultados.
> Parte de LLVM.
> Más información: <https://www.llvm.org/docs/CommandGuide/lit.html>.

- Ejecuta un caso de prueba especificado:

`lit {{ruta/al/archivo_de_prueba.test}}`

- Ejecuta todos los casos de prueba en un directorio especificado:

`lit {{ruta/al/suite_de_pruebas}}`

- Ejecuta todos los escenarios de prueba y comprueba el tiempo de ejecución de cada uno de ellos:

`lit {{ruta/a/suite_de_pruebas}} --time-tests`

- Ejecuta pruebas individuales con Valgrind (comprobación de memoria y prueba de fuga de memoria):

`lit {{ruta/al/archivo_prueba.test}} --vg --vg-leak --vg-args={{args_con_valgrind}}`

# bats

> Bash Automated Testing System: un marco de pruebas compatible con TAP (<https://testanything.org/>) para Bash.
> Más información: <https://bats-core.readthedocs.io/en/stable/usage.html>.

- Ejecuta un guión de prueba BATS y emite los resultados en el formato TAP (Test Anything Protocol):

`bats --tap {{ruta/a/prueba.bats}}`

- Cuenta los casos de prueba de un guión de prueba sin ejecutar ninguna prueba:

`bats --count {{ruta/a/prueba.bats}}`

- Ejecuta casos de prueba BATS en un directorio y sus subdirectorios (archivos con extensión `.bats`):

`bats --recursive {{ruta/al/directorio}}`

- Obtén resultados en un formato específico:

`bats --formatter {{pretty|tap|junit}} {{ruta/a/prueba.bats}}`

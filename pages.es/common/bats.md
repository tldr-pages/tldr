# bats

> Bash Automated Testing System: un marco de pruebas compatible con TAP (<https://testanything.org/>) para Bash.
> Más información: <https://bats-core.readthedocs.io/en/stable/usage.html>.

- Ejecuta un script de prueba BATS y muestra los resultados en el formato [t]AP (Test Anything Protocol):

`bats --tap {{ruta/a/prueba.bats}}`

- [c]ontar casos de prueba de un script de prueba sin ejecutar ninguna prueba:

`bats --count {{ruta/a/prueba.bats}}`

- Ejecuta casos de prueba BATS [r]ecursivamente (archivos con extensión `.bats`):

`bats --recursive {{ruta/a/directorio}}`

- Muestra los resultados en un [f]ormato específico:

`bats --formatter {{pretty|tap|tap13|junit}} {{ruta/a/prueba.bats}}`

- Añade información de [T]iming a las pruebas:

`bats --timing {{ruta/a/prueba.bats}}`

- Ejecuta un número específico de traba[j]os en paralelo (requiere tener instalado GNU `parallel`):

`bats --jobs {{número}} {{ruta/a/prueba.bats}}`

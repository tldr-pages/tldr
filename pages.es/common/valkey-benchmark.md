# valkey-benchmark

> Realizar pruebas de rendimiento en un servidor Valkey.
> Más información: <https://valkey.io/topics/benchmark/>.

- Ejecutar prueba de rendimiento completa:

`valkey-benchmark`

- Ejecutar prueba de rendimiento en un servidor Valkey específico:

`valkey-benchmark -h {{host}} -p {{puerto}} -a {{contraseña}}`

- Ejecutar un subconjunto de pruebas con 100,000 solicitudes predeterminadas:

`valkey-benchmark -h {{host}} -p {{puerto}} -t {{set,lpush}} -n {{100000}}`

- Ejecutar con un script específico:

`valkey-benchmark -n {{100000}} script load "{{valkey.call('set', 'foo', 'bar')}}"`

- Ejecutar prueba de rendimiento usando 100000 claves aleato[r]ias:

`valkey-benchmark -t {{set}} -r {{100000}}`

- Ejecutar prueba de rendimiento usando canalización ([P]ipelining) de 16 comandos:

`valkey-benchmark -n {{1000000}} -t {{set,get}} -P {{16}}`

- Ejecutar prueba de rendimiento en modo silencioso ([q]uiet) y mostrar solo el resultado de consultas por segundo:

`valkey-benchmark -q`

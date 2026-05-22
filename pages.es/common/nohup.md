# nohup

> Permite que un proceso siga ejecutándose cuando se cierra el terminal.
> Más información: <https://www.gnu.org/software/coreutils/manual/html_node/nohup-invocation.html>.

- Ejecuta un proceso que puede seguir ejecutándose tras el cierre del terminal:

`nohup {{comando}} {{argumento1 argumento2 ...}}`

- Ejecuta `nohup` en modo de segundo plano:

`nohup {{comando}} {{argumento1 argumento2 ...}} &`

- Ejecuta un script de intérprete de comandos que puede seguir ejecutándose tras el cierre del terminal:

`nohup {{ruta/al/script.sh}} &`

- Ejecuta un proceso y escribe la salida en un archivo específico:

`nohup {{comando}} {{argumento1 argumento2 ...}} > {{ruta/al/archivo_de_salida}} &`

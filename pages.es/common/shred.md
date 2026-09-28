# shred

> Sobrescribe archivos para eliminar datos de forma segura.
> Más información: <https://www.gnu.org/software/coreutils/manual/html_node/shred-invocation.html>.

- Sobrescribe un archivo:

`shred {{ruta/al/archivo}}`

- Sobrescribe un archivo y mostrar el progreso en pantalla:

`shred {{[-v|--verbose]}} {{ruta/al/archivo}}`

- Sobrescribe un archivo, sustituyendo los datos aleatorios por ceros:

`shred {{[-z|--zero]}} {{ruta/al/archivo}}`

- Sobrescribe un archivo un número específico de veces:

`shred {{[-n|--iterations]}} {{25}} {{ruta/al/archivo}}`

- Sobrescribe un archivo y lo elimina:

`shred {{[-u|--remove]}} {{ruta/al/archivo}}`

- Sobrescribe un archivo 100 veces, añade una sobrescritura final con ceros, eliminar el archivo tras sobrescribirlo y muestra el progreso detallado en pantalla:

`shred {{[-vzu|--verbose --zero --remove]}} {{[-n|--iterations]}} 100 {{ruta/al/archivo}}`

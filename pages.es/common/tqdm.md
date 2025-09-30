# tqdm

> Muestra una barra de progreso a lo largo del tiempo de un comando.
> Más información: <https://tqdm.github.io/docs/cli/>.

- Muestra iteraciones por segundo y usa `stdout` después:

`{{seq 10000000}} | tqdm | {{comando}}`

- Crea una barra de progreso:

`{{seq 10000000}} | tqdm --total {{10000000}} | {{comando}}`

- Crea un archivo a partir de un directorio y utiliza el recuento de archivos de ese directorio para crear una barra de progreso:

`zip {{[-r|--recurse-paths]}} {{ruta/al/archivo.zip}} {{ruta/al/directorio}} | tqdm --total $(find {{ruta/al/directorio}} | wc {{[-l|--líneas]}}) --unit files --null`

- Crea un archivo con tar y crea una barra de progreso (sistema agnóstico, GNU tar usa `stdout` mientras BSD tar usa `stderr`):

`tar vzcf {{ruta/al/archivo.tar.gz}} {{ruta/al/directorio}} 2>&1 | tqdm --total $(find {{ruta/al/directorio}} | wc {{[-l|--líneas]}}) --unit files --null`

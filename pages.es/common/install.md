# install

> Copia archivos y establecer atributos.
> Usualmente utilizado  en archivos Makefile.
> Más información: <https://www.gnu.org/software/coreutils/manual/html_node/install-invocation.html>.

- Copia archivos al destino:

`install {{ruta/al/archivo_fuente1 ruta/al/archivo_fuente2 ...}} {{ruta/al/destino}}`

- Copia archivos al destino, estableciendo su propiedad:

`install {{[-o|--owner]}} {{usuario}} {{ruta/al/archivo_de_origen1 ruta/al/archivo_de_origen2 ...}} {{ruta/al/destino}}`

- Copia archivos al destino, estableciendo su propiedad de grupo:

`install {{[-g|--group]}} {{usuario}} {{ruta/al/archivo_de_origen1 ruta/al/archivo_de_origen2 ...}} {{ruta/al/destino}}`

- Copia archivos al destino, estableciendo su `modo`:

`install {{[-m|--mode]}} {{+x}} {{ruta/al/archivo_de_origen1 ruta/al/archivo_de_origen2 ...}} {{ruta/al/destino}}`

- Copia archivos y aplica las fechas y horas de acceso y modificación de los archivos de origen a los de destino:

`install {{[-p|--preserve-timestamps]}} {{ruta/al/archivo_de_origen1 ruta/al/archivo_de_origen2 ...}} {{ruta/al/destino}}`

- Copia archivos y crea los directorios en el destino si no existen:

`install -D {{ruta/al/archivo_de_origen1 ruta/al/archivo_de_origen2 ...}} {{ruta/al/destino}}`

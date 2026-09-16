# b2sum

> Calcula sumas de comprobación criptográficas BLAKE2.
> Más información: <https://www.gnu.org/software/coreutils/manual/html_node/b2sum-invocation.html>.

- Calcula la suma de comprobación BLAKE2 para uno o más archivos:

`b2sum {{ruta/al/archivo1 ruta/al/archivo2 ...}}`

- Calcula y guarda la lista de sumas de comprobación BLAKE2 en un archivo:

`b2sum {{ruta/al/archivo1 ruta/al/archivo2 ...}} > {{ruta/al/archivo.b2}}`

- Calcula una suma de comprobación BLAKE2 desde `stdin`:

`{{comando}} | b2sum`

- Lee un archivo de sumas de comprobación BLAKE2 y nombres de archivo y verifica que todos los archivos tengan sumas de comprobación coincidentes:

`b2sum {{[-c|--check]}} {{path/to/file.b2}}`

- Muestra solo un mensaje para los archivos que faltan o cuando falla la verificación:

`b2sum {{[-c|--check]}} --quiet {{ruta/al/archivo.b2}}`

- Muestra solo un mensaje cuando falle la verificación, ignorando los archivos que faltan:

`b2sum --ignore-missing {{[-c|--check]}} --quiet {{ruta/al/archivo.b2}}`

- Comprueba una suma de comprobación BLAKE2 conocida de un archivo:

`echo {{suma_de_comprobación_blake2_conocida_del_archivo}} {{ruta/al/archivo}} | b2sum {{[-c|--check]}}`

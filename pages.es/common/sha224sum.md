# sha224sum

> Calcula sumas de comprobación criptográficas SHA224.
> Más información: <https://www.gnu.org/software/coreutils/manual/html_node/sha2-utilities.html>.

- Calcula la suma de comprobación SHA224 para uno o más archivos:

`sha224sum {{ruta/al/archivo1 ruta/al/archivo2 ...}}`

- Calcula y guarda la lista de sumas de comprobación SHA224 en un archivo:

`sha224sum {{ruta/al/archivo1 ruta/al/archivo2 ...}} > {{ruta/al/archivo.sha224}}`

- Calcula una suma de comprobación SHA224 desde `stdin`:

`{{comando}} | sha224sum`

- Lee nombres de archivo y archivo de sumas de comprobación SHA224 y verifica que todos los archivos tengan sumas de comprobación coincidentes:

`sha224sum {{[-c|--check]}} {{ruta/al/archivo.sha224}}`

- Muestra solo un mensaje para los archivos que faltan o cuando falla la verificación:

`sha224sum {{[-c|--check]}} --quiet {{ruta/al/archivo.sha224}}`

- Muestra solo un mensaje cuando falla la verificación, ignorando los archivos que faltan:

`sha224sum --ignore-missing {{[-c|--check]}} --quiet {ruta/al/archivo.sha224}}`

- Comprueba una suma de comprobación SHA224 conocida de un archivo:

`echo {{suma_de_comprobación_sha224_conocida_del_archivo}} {{ruta/al/archivo}} | sha224sum {{[-c|--check]}}`

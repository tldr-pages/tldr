# md5sum

> Calcula sumas de comprobación criptográficas MD5.
> Más información: <https://www.gnu.org/software/coreutils/manual/html_node/md5sum-invocation.html>.

- Calcula la suma de comprobación MD5 de uno o más archivos:

`md5sum {{ruta/al/archivo1 ruta/al/archivo2 ...}}`

- Calcula y guarda la lista de sumas de comprobación MD5 en un archivo:

`md5sum {{ruta/al/archivo1 ruta/al/archivo2 ...}} > {{ruta/al/archivo.md5}}`

- Calcula una suma de comprobación MD5 a partir de `stdin`:

`{{comando}} | md5sum`

- Lee un archivo de sumas de comprobación MD5 y nombres de archivo y verifica que todos los archivos tengan sumas de comprobación coincidentes:

`md5sum {{[-c|--check]}} {{ruta/al/archivo.md5}}`

- Muestra un mensaje solo para los archivos que faltan o cuando falla la verificación:

`md5sum {{[-c|--check]}} --quiet {{ruta/al/archivo.md5}}`

- Muestra un mensaje solo cuando falla la verificación, ignorando los archivos que faltan:

`md5sum --ignore-missing {{[-c|--check]}} --quiet {{ruta/al/archivo.md5}}`

- Comprueba la suma de comprobación MD5 conocida de un archivo:

`echo {{suma_de_comprobación_md5_conocida_del_archivo}} {{ruta/al/archivo}} | md5sum {{[-c|--check]}}`

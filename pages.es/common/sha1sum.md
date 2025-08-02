# sha1sum

> Calcula sumas de comprobación criptográficas SHA1.
> Más información: <https://www.gnu.org/software/coreutils/manual/html_node/sha1sum-invocation.html>.

- Calcula la suma de comprobación SHA1 de uno o más archivos:

`sha1sum {{ruta/al/archivo1 ruta/al/archivo2 ...}}`

- Calcula y guardar la lista de sumas de comprobación SHA1 en un archivo:

`sha1sum {{ruta/al/archivo1 ruta/al/archivo2 ...}} > {{ruta/al/archivo.sha1}}`

- Calcula una suma de comprobación SHA1 a partir de `stdin`:

`{{comando}} | sha1sum`

- Lee un archivo de sumas de comprobación SHA1 y nombres de archivo y verifica que todos los archivos tengan sumas de comprobación coincidentes:

`sha1sum {{[-c|--check]}} {{ruta/al/archivo.sha1}}`

- Solo muestra un mensaje cuando faltan archivos o cuando falla la verificación:

`sha1sum {{[-c|--check]}} --quiet {{ruta/al/archivo.sha1}}`

- Solo muestra un mensaje cuando falla la verificación, ignorando los archivos que faltan:

`sha1sum --ignore-missing {{[-c|--check]}} --quiet {{ruta/a/archivo.sha1}}`

- Comprueba una suma de comprobación SHA1 conocida de un archivo:

`echo {{suma_de_verificación_sha1_conocida_del_archivo}} {{ruta/al/archivo}} | sha1sum {{[-c|--check]}}`

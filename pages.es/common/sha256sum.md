# sha256sum

> Calcula sumas de comprobación criptográficas SHA256.
> Más información: <https://www.gnu.org/software/coreutils/manual/html_node/sha2-utilities.html>.

- Calcula la suma de comprobación SHA256 de uno o varios archivos:

`sha256sum {{ruta/al/archivo1 ruta/al/archivo2 ...}}`

- Calcula y guarda la lista de sumas de comprobación SHA256 en un archivo:

`sha256sum {{ruta/al/archivo1 ruta/al/archivo2 ...}} >{{ruta/al/archivo.sha256}}`

- Calcula una suma de comprobación SHA256 a partir de `stdin`:

`{{comando}} | sha256sum`

- Lee un archivo con sumas de comprobación SHA256 y nombres de archivo, y verifica que todos los archivos tengan sumas de comprobación coincidentes:

`sha256sum {{[-c|--check]}} {{ruta/al/archivo.sha256}}`

- Muestra un mensaje solo si faltan archivos o cuando falla la verificación:

`sha256sum {{[-c|--check]}} --quiet {{ruta/al/archivo.sha256}}`

- Muestra un mensaje únicamente cuando falle la verificación, ignorando los archivos que falten:

`sha256sum --ignore-missing {{[-c|--check]}} --quiet {{ruta/al/archivo.sha256}}`

- Comprueba la suma de comprobación SHA256 conocida de un archivo:

`echo {{suma_de_comprobación_sha256_conocida_del_archivo}} {{ruta/al/archivo}} | sha256sum {{[-c|--check]}}`

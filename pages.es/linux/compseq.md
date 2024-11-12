# compseq

> Calcula la composición de palabras únicas en secuencias.
> Más información: <https://www.bioinformatics.nl/cgi-bin/emboss/help/compseq/>.

- Cuenta frecuencias observadas de palabras en un archivo FASTA, proporcionando valores de parámetros interactivamente:

`compseq {{ruta/al/archivo.fasta}}`

- Cuenta frecuencias observadas de pares de aminoácidos en un archivo FASTA, y guarda el resultado en un archivo de texto:

`compseq {{ruta/al/archivo_proteina.fasta}} -word 2 {{ruta/al/archivo_de_salida.comp}}`

- Cuenta las frecuencias observadas de hexanucleótidos en un archivo FASTA, luego guarda el resultado en un archivo de texto e ignora los recuentos cero:

`compseq {{ruta/al/archivo_de_entrada.fasta}} -word 6 {{ruta/al/archivo_de_salida.comp}} -nozero`

- Cuenta las frecuencias observadas de codones en un marco de lectura concreto, ignorando cualquier recuento superpuesto (es decir, desplaza la ventana en longitud de palabra 3):

`compseq -sequence {{ruta/al/archivo_de_ingreso_rna.fasta}} -word 3 {{ruta/al/archivo_de_salida.comp}} -nozero -frame {{1}}`

- Cuenta las frecuencias observadas de codones desplazados en 3 posiciones; ignorando los recuentos superpuestos (debería informar de todos los codones excepto el primero):

`compseq -sequence {{ruta/al/archivo_de_ingreso_rna.fasta}} -word 3 {{ruta/al/archivo_de_salida.comp}} -nozero -frame 3`

- Cuenta tripletes de aminoácidos en un archivo FASTA y compara con una ejecución anterior de `compseq` para calcular los valores de frecuencia esperados y normalizados:

`compseq -sequence {{ruta/al/proteoma_humano.fasta}} -word 3 {{ruta/al/archivo_salida1.comp}} -nozero -infile {{ruta/al/archivo_de_salida2.comp}}`

- Aproxima el comando anterior sin un archivo previamente preparado, calculando las frecuencias esperadas usando las frecuencias de una sola base/residuo en la(s) secuencia(s) de entrada suministrada(s):

`compseq -sequence {{ruta/al/proteoma_humano.fasta}} -word 3 {{ruta/al/archivo_de_salida.comp}} -nozero -calcfreq`

- Muestra ayuda (utiliza `-help -verbose` para obtener más información sobre los calificadores asociados y generales):

`compseq -help`

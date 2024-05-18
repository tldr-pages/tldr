# bwa

> Herramienta de alineación Burrows-Wheeler.
> Mapeador de secuencias de ADN cortas y poco divergentes frente a un gran genoma de referencia, como el genoma humano.
> Más información: <https://github.com/lh3/bwa>.

- Indexa el genoma de referencia:

`bwa index {{ruta/a/referencia.fa}}`

- Mapea las lecturas de un solo extremo (secuencias) al genoma indexado utilizando 32 subprocesos y comprime el resultado para ahorrar espacio:

`bwa mem -t 32 {{ruta/a/referencia.fa}} {{ruta/a/lectura_solo_extremo.fq.gz}} | gzip > {{ruta/a/alineamiento_solo_extremo.sam.gz}}`

- Mapea las lecturas del par final (secuencias) al genoma indexado usando 32 subprocesos y comprime el resultado para ahorrar espacio:

`bwa mem -t 32 {{ruta/a/referencia.fa}} {{ruta/a/lectura_par_final_1.fq.gz}} {{ruta/a/lectura_par_final_2.fq.gz}} | gzip > {{ruta/a/alineamiento_par_final.sam.gz}}`

- Mapea las lecturas del par final (secuencias) al genoma indexado usando 32 subprocesos con [M]arcadores divididos más cortos como secundarios para la compatibilidad del archivo SAM de salida con el software Picard y luego comprime el resultado:

`bwa mem -M -t 32 {{ruta/a/referencia.fa}} {{ruta/a/lectura_par_final_1.fq.gz}} {{ruta/a/lectura_par_final_2.fq.gz}} | gzip > {{ruta/a/alineamiento_par_final.sam.gz}}`

- Mapea las lecturas finales del par (secuencias) al genoma indexado usando 32 subprocesos con [C]omentarios FASTA/Q  (p. ej. BC:Z:CGTAC) anexando a un resultado comprimido:

`bwa mem -C -t 32 {{ruta/a/referencia.fa}} {{ruta/a/lectura_par_final_1.fq.gz}} {{ruta/a/lectura_par_final_2.fq.gz}} | gzip > {{ruta/a/lectura_par_final.sam.gz}}`

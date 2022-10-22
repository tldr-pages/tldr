# bedtools

> Un coltellino svizzero di strumenti per analisi genomica.
> Usato per intersecare, raggruppare, convertire e contare dati in formato BAM, BED, GFF/GTF, VCF.
> Maggiori informazioni: <https://bedtools.readthedocs.io>.

- Interseca i fili genetici delle sequenze contenute in due file diversi e salva il risultato:

`bedtools intersect -a {{percorso/del/file_1}} -b {{percorso/del/file_2}} -s > {{percorso/del/file_output}}`

- Interseca due file unendo il risultato a sinistra, ovvero riporta ogni feature da {{file_1}} e NULL dove non c'è sovrapposizione con {{file_2}}:

`bedtools intersect -a {{percorso/del/file_1}} -b {{percorso/del/file_2}} -lof > {{percorso/del/file_output}}`

- Usa un algoritmo più efficiente per intersecare due file precedentemente ordinati:

`bedtools intersect -a {{percorso/del/file_1}} -b {{percorso/del/file_2}} -sorted > {{percorso/del/file_output}}`

- Raggruppa file in base alle prime tre e la quinta colonna e raggruppa la sesta colonna sommandola:

`bedtools groupby -i {{percorso/del/file}} -c 1-3,5 -g 6 -o sum`

- Converti da formato BAM a BED:

`bedtools bamtobed -i {{percorso/del/file}}.bam > {{percorso/del/file}}.bed`

- Trova per tutte le proprietà in {{file_1}} la più vicina in {{file_2}} e scrivi la loro distanza in una ulteriore colonna (i file in input devono essere ordinati):

`bedtools closest -a {{percorso/del/file_1}}.bed -b {{percorso/del/file_2}}.bed -d`

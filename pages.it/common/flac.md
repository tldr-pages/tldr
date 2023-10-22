# flac

> Codifica, decodifica e controlla file flac.
> Maggiori informazioni: <https://xiph.org/flac>.

- Converte un file wav in un file flac (questo creerà un file flac nella medesima posizione del file wav):

`flac {{percorso/del/file.wav}}`

- Codifica un file wav in flac, specificando il nome del risultato:

`flac -o {{percorso/del/file_compresso.flac}} {{percorso/del/file_originale.wav}}`

- Decodifica un file wav in flac, specificando il nome del risultato:

`flac -d -o {{percorso/del/file_decompresso.wav}} {{percorso/del/file_originale.flac}}`

- Controlla che un file flac sia codificato correttamente:

`flac -t {{percorso/del/file.flac}}`

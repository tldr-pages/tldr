# flac

> Codifica, decodifica e controlla file flac.
> Maggiori informazioni: <https://xiph.org/flac>.

- Converte un file wav in un file flac(questo creerà un file flac nella medesima posizione del file wav):

`flac {{percorso/al/file.wav}}`

- Codifica un file wav in flac, specificando il nome del risultato:

`flac -o {{percorso/all/output.flac}} {{percorso/al/file.wav}}`

- Decodifica un file wav in flac, specificando il nome del risultato:

`flac -d -o {{percorso/all/output.wav}} {{percorso/al/file.flac}}`

- Controlla che un file flac sia codificato correttamente:

`flac -t {{percorso/al/file.flac}}`

# binwalk

> Strumento per l'analisi di file binari.
> Maggiori informazioni: <https://github.com/ReFirmLabs/binwalk>.

- Scansiona un file binario:

`binwalk {{percorso/del/file}}`

- Estrae file da un binario, specificando la directory di output:

`binwalk --extract --directory {{directory_di_output}} {{percorso/del/file}}`

- Estrae file in maniera ricorsiva a partire da un binario, limitando la profondità di ricorsione a 2 livelli:

`binwalk --extract --matryoshka --depth {{2}} {{percorso/del/file}}`

- Estrae file da un binario utilizzando una particolare firma (ad esempio il MIME Type):

`binwalk --dd '{{png image:png}}' {{percorso/del/file}}`

- Analizza l'entropia di un binario e salva il grafico con lo stesso filename del binario, con l'estensione `.png` in fondo:

`binwalk --entropy --save {{percorso/del/file}}`

- Combina analisi di entropia, firme e opcode in un unico comando:

`binwalk --entropy --signature --opcodes {{percorso/del/file}}`

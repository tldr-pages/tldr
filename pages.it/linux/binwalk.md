# binwalk

> Strumento per l'analisi di file binari.
> Maggiori informazioni: <https://github.com/ReFirmLabs/binwalk>.

- Scansiona un file binario:

`binwalk {{percorso/a/file}}`

- Estrae file da un binario, specificando la cartella di output:

`binwalk --extract --directory {{cartella_di_output}} {{percorso/a/file}}`

- Estrae file in maniera ricorsiva a partire da un binario, limitando la profondità di ricorsione a 2 livelli:

`binwalk --extract --matryoshka --depth {{2}} {{percorso/a/file}}`

- Estrae file da un binario utilizzando una particolare firma (ad esempio il MIME Type):

`binwalk --dd '{{png image:png}}' {{percorso/a/file}}`

- Analizza l'entropia di un binario e salva il grafico con lo stesso filename del binario, con l'estensione `.png` in fondo:

`binwalk --entropy --save {{percorso/a/file}}`

- Combina analisi di entropia, firme e opcode in un unico comando:

`binwalk --entropy --signature --opcodes {{percorso/a/file}}`

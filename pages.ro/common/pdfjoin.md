# pdfjoin

> Utilitar de îmbinare PDF bazat pe pdfjam.
> Mai multe informaţii: <https://github.com/rrthomas/pdfjam-extras>

- Îmbinaţi două PDF-uri într-unul cu sufixul implicit „alăturat”:

`pdfjoin {{path/to/file1.pdf}} {{path/to/file2.pdf}}`

- Îmbinați prima pagină a fiecărui fișier dat împreună:

`pdfjoin {{path/to/file1.pdf path/to/file2.pdf ...}} {{1}} --outfile {{output_file}}`

- Salvați paginile 3 la 5 urmate de pagina 1 într-un PDF nou cu sufix personalizat:

`pdfjoin {{path/to/file.pdf}} {{3-5,1}} --suffix {{rearranged}}`

- Îmbinarea subrangelor de pagină din două PDF-uri:

`pdfjoin {/path/to/file1.pdf}} {{2-}} {{file2}} {{last-3}} --outfile {{output_file}}`

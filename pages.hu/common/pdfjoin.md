# pdfjoin

> PDF egyesítő segédprogram a pdfjam alapján. További információ: <https://github.com/rrthomas/pdfjam-extras>.

- Két PDF egyesítése egy PDF-be az alapértelmezett "joined" utótaggal:

`pdfjoin {{path/to/file1.pdf}} {{path/to/file2.pdf}}`

- Egyesíti az adott fájlok első oldalát:

`pdfjoin {{path/to/file1.pdf path/to/file2.pdf ...}} {{1}} --outfile {{output_file}}`

- A 3-5. oldal és az 1. oldal után az 1. oldal mentése egy új PDF-be egyéni utótaggal:

`pdfjoin {{path/to/file.pdf}} {{3-5,1}} --suffix {{rearranged}}`

- Oldalrészek egyesítése két PDF-ből:

`pdfjoin {/path/to/file1.pdf}} {{2-}} {{file2}} {{last-3}} --outfile {{output_file}}`

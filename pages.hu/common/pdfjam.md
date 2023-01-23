# pdfjam

> Shell frontend a LaTeX pdfpages csomaghoz a PDF-ek keveréséhez. További információ: <https://github.com/rrthomas/pdfjam>.

- Két (vagy több) PDF összevonása:

`pdfjam {{path/to/file1.pdf}} {{path/to/file2.pdf}} --outfile {{path/to/output_file.pdf}}`

- Egyesíti az egyes fájlok első oldalát:

`pdfjam {{files...}} 1 --outfile {{path/to/output_file.pdf}}`

- Két PDF részoldalak összevonása:

`pdfjam {{path/to/file1.pdf 3-5,1}} {{path/to/file2.pdf 4-6}} --outfile {{path/to/output_file.pdf}}`

- Egy A4-es oldal aláírása (más formátumok esetén a delta magasságának beállítása) szkennelt aláírással, a lapok egymásra helyezésével:

`pdfjam {{path/to/file.pdf}} {{path/to/signature}} --fitpaper true --outfile {{path/to/signed.pdf}} --nup "{{1x2}}" --delta "{{0 -842pt}}"`

- Rendezze az oldalakat a bemeneti fájlból egy díszes 2x2-es rácsba:

`pdfjam {{path/to/file.pdf}} --nup {{2x2}} --suffix {{4up}} --preamble '{{\usepackage{fancyhdr} \pagestyle{fancy}}}'`

- Fordítsa meg az oldalak sorrendjét az egyes adott fájlokon belül, és kapcsolja össze őket:

`pdfjam {{files...}} {{last-1}} --suffix {{reversed}}`

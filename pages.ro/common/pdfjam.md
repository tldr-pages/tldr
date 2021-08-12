# pdfjam

> Interfață shell pentru pachetul PDFpages LaTeX pentru amestecarea PDF-urilor.
> Mai multe informaţii: <https://github.com/rrthomas/pdfjam>

- Îmbinaţi două (sau mai multe) PDF-uri:

`pdfjam {{path/to/file1.pdf}} {{path/to/file2.pdf}} --outfile {{path/to/output_file.pdf}}`

- Îmbinați prima pagină a fiecărui fișier împreună:

`pdfjam {{files...}} 1 --outfile {{path/to/output_file.pdf}}`

- Îmbinarea subrangelor din două PDF-uri:

`pdfjam {{path/to/file1.pdf 3-5,1}} {{path/to/file2.pdf 4-6}} --outfile {{path/to/output_file.pdf}}`

- Semnați o pagină A4 (ajustați delta la înălțime pentru alte formate) cu o semnătură scanată prin suprapunerea acestora:

`pdfjam {{path/to/file.pdf}} {{path/to/signature}} --fitpaper true --outfile {{path/to/signed.pdf}} --nup "{{1x2}}" --delta "{{0 -842pt}}"`

- Aranjați paginile din fișierul de intrare într-o grilă 2x2 fantezie:

`pdfjam {{path/to/file.pdf}} --nup {{2x2}} --suffix {{4up}} --preamble '{{\usepackage{fancyhdr} \pagestyle{fancy}}}'`

- Inversați ordinea paginilor din fiecare fișier dat și concatenați-le:

`pdfjam {{files...}} {{last-1}} --suffix {{reversed}}`

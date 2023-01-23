# blastn

> Nukleotid-nukleotid BLAST. További információ: <https://www.ncbi.nlm.nih.gov/books/NBK279684/table/appendices.T.blastn_application_options/>.

- Két vagy több szekvencia összehangolása megablast segítségével (alapértelmezett), 1e-9-es e-érték küszöbértékkel, páros kimeneti formátumban (alapértelmezett):

`blastn -query {{query.fa}} -subject {{subject.fa}} -evalue {{1e-9}}`

- Két vagy több szekvencia összehangolása blastn használatával:

`blastn -task blastn -query {{query.fa}} -subject {{subject.fa}}`

- Két vagy több szekvencia összehangolása, egyéni táblázatos kimeneti formátum, kimenet fájlba:

`blastn -query {{query.fa}} -subject {{subject.fa}} -outfmt {{'6 qseqid qlen qstart qend sseqid slen sstart send bitscore evalue pident'}} -out {{output.tsv}}`

- Nukleotid-adatbázisok keresése nukleotid-lekérdezéssel, 16 szál (CPU) használata a BLAST-kereséshez, legfeljebb 10 összehangolt szekvencia megtartása:

`blastn -query {{query.fa}} -db {{path/to/blast_db}} -num_threads {{16}} -max_target_seqs {{10}}`

- Távoli, nem redundáns nukleotid-adatbázis keresése nukleotid-lekérdezéssel:

`blastn -query {{query.fa}} -db {{nt}} -remote`

- Súgó megjelenítése (a részletes súgóhoz használja a `-help` címet):

`blastn -h`

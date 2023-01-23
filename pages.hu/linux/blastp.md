# blastp

> Protein-Protein BLAST. További információ: <https://www.ncbi.nlm.nih.gov/books/NBK279684/table/appendices.T.blastp_application_options/>.

- Két vagy több szekvencia összehangolása blastp segítségével, 1e-9-es e-érték küszöbértékkel, páros kimeneti formátumban, képernyőre történő kimenet:

`blastp -query {{query.fa}} -subject {{subject.fa}} -evalue {{1e-9}}`

- Két vagy több szekvencia összehangolása blastp-fast használatával:

`blastp -task blastp-fast -query {{query.fa}} -subject {{subject.fa}}`

- Két vagy több szekvencia összehangolása, egyéni táblázatos kimeneti formátum, kimenet fájlba:

`blastp -query {{query.fa}} -subject {{subject.fa}} -outfmt '{{6 qseqid qlen qstart qend sseqid slen sstart send bitscore evalue pident}}' -out {{output.tsv}}`

- Fehérje adatbázisok keresése fehérje lekérdezéssel, 16 szál használata a BLAST keresésben, maximum 10 igazított szekvencia megtartása:

`blastp -query {{query.fa}} -db {{blast_database_name}} -num_threads {{16}} -max_target_seqs {{10}}`

- Keresés távoli, nem redundáns fehérjeadatbázisban egy fehérjekérdés segítségével:

`blastp -query {{query.fa}} -db {{nr}} -remote`

- Súgó megjelenítése (a részletes súgóhoz használja a `-help` címet):

`blastp -h`

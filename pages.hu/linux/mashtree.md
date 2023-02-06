# mashtree

> Gyors fát készít genomokból, filogeniát nem. További információ: <https://github.com/lskatz/mashtree>.

- A mashtree leggyorsabb módszere fastq és/vagy fasta fájlokból fa létrehozására több szál felhasználásával, egy newick fájlba pipingolva:

`mashtree --numcpus {{12}} {{*.fastq.gz}} {{*.fasta}} > {{mashtree.dnd}}`

- A legpontosabb módszer a mashtree-ben a fa létrehozására fastq és/vagy fasta fájlokból több szál felhasználásával, newick fájlba való átvezetéssel:

`mashtree --mindepth {{0}} --numcpus {{12}} {{*.fastq.gz}} {{*.fasta}} > {{mashtree.dnd}}`

- A legpontosabb módszer egy fa létrehozására bizalmi értékekkel (vegye figyelembe, hogy a `mashtree` magának az opciónak a `--` jobb oldalán kell lennie):

`mashtree_bootstrap.pl --reps {{100}} --numcpus {{12}} {{*.fastq.gz}} -- --min-depth {{0}} > {{mashtree.bootstrap.dnd}}`

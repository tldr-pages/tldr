# nextclade

> Bioinformatikai eszköz vírusgenom-összehasonlításhoz, kládbeosztáshoz és qc-ellenőrzéshez. További információ: <https://docs.nextstrain.org/projects/nextclade/en/stable/user/nextclade-cli.html>.

- TSV-jelentés készítése, a legújabb \[d\]atkészlet automatikus letöltése:

`nextclade run -d {{dataset_name}} {{path/to/fasta}} -t {{path/to/output_tsv}}`

- Az összes rendelkezésre álló adatkészlet listázása:

`nextclade dataset list`

- A legfrissebb SARS-CoV-2 adatkészlet letöltése:

`nextclade dataset get --name sars-cov-2 --output-dir {{path/to/directory}}`

- Letöltött \[D\]ataset használata, az összes \[O\]utput előállítása:

`nextclade run -D {{path/to/dataset_dir}} -O {{path/to/output_dir}} {{path/to/dataset_dir/sequences.fasta}}`

- Futtatás több fájlon:

`nextclade run -d {{dataset_name}} -t {{path/to/output_tsv}} -- {{path/to/input_fasta_1 path/to/input_fasta_2 ...}}`

- Próbálja meg a fordított kiegészítést, ha a szekvencia nem illeszkedik:

`nextclade run --retry-reverse-complement -d {{dataset_name}} -t {{path/to/output_tsv}} {{path/to/input_fasta}}`

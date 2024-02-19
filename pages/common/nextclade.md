# nextclade

> Bioinformatics tool for virus genome alignment, clade assignment and qc checks.
> More information: <https://docs.nextstrain.org/projects/nextclade/en/stable/user/nextclade-cli/index.html>.

- Align sequences to user provided [r]eference, [o]utputting the alignment to a file:

`nextclade run {{path/to/sequences.fa}} -r {{path/to/reference.fa}} -o {{path/to/alignment.fa}}`

- Create a [t]SV report, auto-downloading the latest [d]ataset:

`nextclade run {{path/to/fasta}} -d {{dataset_name}} -t {{path/to/report.tsv}}`

- List all available datasets:

`nextclade dataset list`

- Download the latest SARS-CoV-2 dataset:

`nextclade dataset get --name sars-cov-2 --output-dir {{path/to/directory}}`

- Use a downloaded [D]ataset, producing all [O]utputs:

`nextclade run -D {{path/to/dataset_dir}} -O {{path/to/output_dir}} {{path/to/sequences.fasta}}`

- Run on multiple files:

`nextclade run -d {{dataset_name}} -t {{path/to/output_tsv}} -- {{path/to/input_fasta_1 path/to/input_fasta_2 ...}}`

- Try reverse complement if sequence does not align:

`nextclade run --retry-reverse-complement -d {{dataset_name}} -t {{path/to/output_tsv}} {{path/to/input_fasta}}`

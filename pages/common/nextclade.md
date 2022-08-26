# nextclade

> Bioinformatics tool for virus genome alignment, clade assignment and qc checks.
> More information: <https://docs.nextstrain.org/projects/nextclade/en/stable/user/nextclade-cli.html>.

- Create a TSV report, auto-downloading the latest [d]ataset:

`nextclade run -d {{dataset_name}} {{path/to/fasta}} -t {{path/to/output_tsv}}`

- List all available datasets:

`nextclade dataset list`

- Download the latest SARS-CoV-2 dataset:

`nextclade dataset get --name sars-cov-2 --output-dir {{path/to/directory}}`

- Use a downloaded [D]ataset, producing all [O]utputs:

`nextclade run -D {{path/to/dataset_dir}} -O {{path/to/output_dir}} {{path/to/dataset_dir/sequences.fasta}}`

- Run on multiple files:

`nextclade run -d {{dataset_name}} -t {{path/to/output_tsv}} -- {{path/to/input_fasta_1 path/to/input_fasta_2 ...}}`

- Try reverse complement if sequence does not align:

`nextclade run --retry-reverse-complement -d {{dataset_name}} -t {{path/to/output_tsv}} {{path/to/input_fasta}}`

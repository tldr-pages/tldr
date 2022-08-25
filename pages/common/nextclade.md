# nextclade

> Bioinformatics tool for virus genome alignment, clade assignment and qc checks.
> More information: <https://docs.nextstrain.org/projects/nextclade/en/stable/user/nextclade-cli.html>.

- Create TSV report, auto-downloading the latest [d]ataset:

`nextclade run -d {{dataset_name}} {{path/to/fasta}} -t {{path/to/output_tsv}}`

- List all available datasets:

`nextclade dataset list`

- Download latest SARS-CoV-2 dataset:

`nextclade dataset get --name sars-cov-2 --output-dir {{path/to/directory}}`

- Use a downloaded [D]ataset, producing all [O]utputs:

`nextclade run -D {{path/to/dataset-dir}} -O {{output-dir}} {{path/to/dataset-dir/sequences.fasta}}`

- Run on multiple files:

`nextclade run -d {{dataset-name}} -t {{path/to/output-tsv}} -- {{input-fasta-1}} {{input-fasta-2}}`

- Try reverse complement if sequence does not align:

`nextclade run --retry-reverse-complement -d {{dataset-name}} -t {{path/to/output-tsv}} {{input-fasta}}`

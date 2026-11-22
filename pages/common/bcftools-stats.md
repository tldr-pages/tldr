# bcftools stats

> Generate statistics from VCF and BCF files, which can be plotted with `plot-vcfstats`.
> See also: `bcftools`.
> More information: <https://samtools.github.io/bcftools/bcftools.html#stats>.

- Generate statistics for a file and save them:

`bcftools stats {{path/to/input.vcf.gz}} > {{path/to/stats.txt}}`

- Display the summary numbers (samples, records, SNPs, indels, etc.):

`bcftools stats {{path/to/input.vcf.gz}} | grep ^SN`

- Include per-sample statistics for all samples:

`bcftools stats {{[-s|--samples]}} - {{path/to/input.vcf.gz}} > {{path/to/stats.txt}}`

- Compare two indexed files, reporting statistics for shared and unique sites:

`bcftools stats {{path/to/a.vcf.gz}} {{path/to/b.vcf.gz}} > {{path/to/stats.txt}}`

- Generate statistics only for sites that pass all filters:

`bcftools stats {{[-f|--apply-filters]}} PASS {{path/to/input.vcf.gz}} > {{path/to/stats.txt}}`

- Generate statistics with a reference genome to report indel context:

`bcftools stats {{[-F|--fasta-ref]}} {{path/to/reference.fa}} {{path/to/input.vcf.gz}} > {{path/to/stats.txt}}`

- Plot the statistics into a directory of charts:

`plot-vcfstats {{[-p|--prefix]}} {{path/to/output_directory}} {{path/to/stats.txt}}`

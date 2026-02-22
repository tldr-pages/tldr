# bcftools

> Tools for manipulating VCF and BCF files.
> More information: <https://samtools.github.io/bcftools/bcftools.html>.

- View BCF file and convert to [v]CF on `stdout`:

`bcftools view {{path/to/input.bcf}} {{[-O|--output-type]}} v`

- Sort a VCF file variants by chromosome and position, output to a [b]CF file, and index the sorted output:

`bcftools sort {{path/to/input.vcf.gz}} {{[-O|--output-type]}} b {{[-o|--output]}} {{path/to/sorted.bcf}} {{[-W|--write-index]}}`

- Concatenate sorted VCF files that share the same samples to [z]ipped VCF on `stdout`:

`bcftools concat {{path/to/chr1.vcf.gz path/to/chr2.vcf.gz ...}} {{[-O|--output-type]}} z`

- Filter for low quality variants and annotate with "LowQual" tag in the FILTER column:

`bcftools filter {{[-e|--exclude]}} 'QUAL<20' {{[-s|--soft-filter]}} LowQual {{path/to/input.vcf.gz}}`

- Add annotated columns from a tabix-indexed table on `stdout`:

`bcftools annotate {{[-a|--annotations]}} {{path/to/annotations.tsv.gz}} {{[-c|--columns]}} CHROM,POS,REF,ALT,INFO/AF {{path/to/input.vcf.gz}}`

- Output variant [i]nter[sec]tion between VCF files using 4 threads:

`bcftools isec {{path/to/a.vcf.gz path/to/b.vcf.gz ...}} --threads 4 {{[-o|--output]}} {{path/to/intersection.vcf}}`

- Merge non-overlapping samples from vcf files without indices on `stdout`:

`bcftools merge {{path/to/cohort1.vcf.gz}} {{path/to/cohort2.vcf.gz}} --no-index`

- Create index for a bgzipped VCF file on `stdout`:

`bcftools index {{path/to/input.vcf.gz}}`

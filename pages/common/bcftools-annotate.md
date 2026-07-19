# bcftools annotate

> Add, remove, or overwrite VCF/BCF annotations.
> See also: `bcftools`.
> More information: <https://samtools.github.io/bcftools/bcftools.html#annotate>.

- Add annotation columns from a tabix-indexed table:

`bcftools annotate {{[-a|--annotations]}} {{path/to/annotations.tsv.gz}} {{[-c|--columns]}} CHROM,POS,REF,ALT,INFO/AF {{path/to/input.vcf.gz}} {{[-o|--output]}} {{path/to/output.vcf.gz}}`

- Remove specific INFO and FORMAT fields:

`bcftools annotate {{[-x|--remove]}} INFO/DP,FORMAT/PL {{path/to/input.vcf.gz}} {{[-o|--output]}} {{path/to/cleaned.vcf.gz}}`

- Rename an annotation key:

`bcftools annotate {{[-r|--rename-annots]}} {{INFO/OLD:=INFO/NEW}} {{path/to/input.vcf.gz}} {{[-o|--output]}} {{path/to/renamed.vcf.gz}}`

- Set ID fields from a tab-delimited file:

`bcftools annotate {{[-a|--annotations]}} {{path/to/ids.tsv.gz}} {{[-c|--columns]}} CHROM,POS,ID {{path/to/input.vcf.gz}} {{[-o|--output]}} {{path/to/with-ids.vcf.gz}}`

- Write compressed BCF output with an index:

`bcftools annotate {{[-a|--annotations]}} {{path/to/annotations.tsv.gz}} {{[-c|--columns]}} CHROM,POS,REF,ALT,INFO/AF {{path/to/input.vcf.gz}} {{[-Ob|--output-type]}} b {{[-o|--output]}} {{path/to/output.bcf}} {{[-W|--write-index]}}`

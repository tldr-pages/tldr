# bcftools view

> View, subset, filter, and convert VCF and BCF files.
> See also: `bcftools`, `bcftools query`.
> More information: <https://samtools.github.io/bcftools/bcftools.html#view>.

- Display a VCF or BCF file without its header:

`bcftools view {{[-H|--no-header]}} {{path/to/input.vcf.gz}}`

- Display only the header of a file:

`bcftools view {{[-h|--header-only]}} {{path/to/input.vcf.gz}}`

- Convert a VCF file to a compressed BCF file:

`bcftools view {{path/to/input.vcf}} {{[-O|--output-type]}} b {{[-o|--output]}} {{path/to/output.bcf}}`

- Extract variants in a specific region from an indexed file:

`bcftools view {{[-r|--regions]}} {{chr1:10000-20000}} {{path/to/input.vcf.gz}}`

- Keep only specific samples:

`bcftools view {{[-s|--samples]}} {{sample1,sample2,...}} {{path/to/input.vcf.gz}}`

- Keep only SNPs, excluding indels and other variant types:

`bcftools view {{[-v|--types]}} snps {{path/to/input.vcf.gz}}`

- Keep only sites matching an expression:

`bcftools view {{[-i|--include]}} '{{QUAL>=30 && INFO/DP>10}}' {{path/to/input.vcf.gz}}`

- Keep only biallelic sites and write a compressed VCF file:

`bcftools view {{[-m|--min-alleles]}} 2 {{[-M|--max-alleles]}} 2 {{path/to/input.vcf.gz}} {{[-O|--output-type]}} z {{[-o|--output]}} {{path/to/output.vcf.gz}}`

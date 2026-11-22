# bcftools query

> Extract fields from VCF and BCF files in a user-defined format.
> See also: `bcftools`, `bcftools view`.
> More information: <https://samtools.github.io/bcftools/bcftools.html#query>.

- Print the chromosome, position, reference allele, and alternate alleles of each site:

`bcftools query {{[-f|--format]}} '%CHROM\t%POS\t%REF\t%ALT\n' {{path/to/input.vcf.gz}}`

- Print the genotype of every sample at each site:

`bcftools query {{[-f|--format]}} '%CHROM\t%POS[\t%GT]\n' {{path/to/input.vcf.gz}}`

- Print a header line naming the output columns:

`bcftools query {{[-HH|--print-header]}} {{[-f|--format]}} '%CHROM\t%POS[\t%GT]\n' {{path/to/input.vcf.gz}}`

- List the sample names in a file:

`bcftools query {{[-l|--list-samples]}} {{path/to/input.vcf.gz}}`

- Print fields only for sites matching an expression:

`bcftools query {{[-i|--include]}} '{{INFO/DP>20}}' {{[-f|--format]}} '%CHROM\t%POS\t%INFO/DP\n' {{path/to/input.vcf.gz}}`

- Print fields for specific samples in a specific region of an indexed file:

`bcftools query {{[-r|--regions]}} {{chr1:10000-20000}} {{[-s|--samples]}} {{sample1,sample2,...}} {{[-f|--format]}} '%POS[\t%GT]\n' {{path/to/input.vcf.gz}}`

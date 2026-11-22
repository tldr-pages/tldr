# bcftools norm

> Left-align and normalize indels, check reference alleles, and split or join multiallelic sites in VCF and BCF files.
> See also: `bcftools`.
> More information: <https://samtools.github.io/bcftools/bcftools.html#norm>.

- Left-align and normalize indels against a reference genome:

`bcftools norm {{[-f|--fasta-ref]}} {{path/to/reference.fa}} {{path/to/input.vcf.gz}} {{[-o|--output]}} {{path/to/output.vcf}}`

- Split multiallelic sites into multiple biallelic records:

`bcftools norm {{[-m|--multiallelics]}} -both {{path/to/input.vcf.gz}}`

- Join biallelic records at the same position into multiallelic sites:

`bcftools norm {{[-m|--multiallelics]}} +both {{path/to/input.vcf.gz}}`

- Normalize indels and exclude sites whose reference allele does not match the reference genome:

`bcftools norm {{[-f|--fasta-ref]}} {{path/to/reference.fa}} {{[-c|--check-ref]}} x {{path/to/input.vcf.gz}}`

- Remove exact duplicate records:

`bcftools norm {{[-d|--rm-dup]}} exact {{path/to/input.vcf.gz}}`

- Split multiallelic sites, normalize, and write a compressed VCF file:

`bcftools norm {{[-m|--multiallelics]}} -both {{[-f|--fasta-ref]}} {{path/to/reference.fa}} {{path/to/input.vcf.gz}} {{[-O|--output-type]}} z {{[-o|--output]}} {{path/to/output.vcf.gz}}`

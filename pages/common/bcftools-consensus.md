# bcftools consensus

> Create consensus sequence by applying VCF variants to a reference FASTA.
> See also: `bcftools`.
> More information: <https://samtools.github.io/bcftools/bcftools.html#consensus>.

- Apply variants to a reference FASTA and write the consensus sequence:

`bcftools consensus {{[-f|--fasta-ref]}} {{path/to/reference.fa}} {{path/to/variants.vcf.gz}} > {{path/to/consensus.fa}}`

- Apply only the first haplotype of heterozygous genotypes:

`bcftools consensus {{[-f|--fasta-ref]}} {{path/to/reference.fa}} {{[-H|--haplotype]}} 1 {{path/to/variants.vcf.gz}} > {{path/to/hap1.fa}}`

- Mask reference positions with missing genotypes using `N`:

`bcftools consensus {{[-f|--fasta-ref]}} {{path/to/reference.fa}} {{[-M|--missing]}} N {{path/to/variants.vcf.gz}} > {{path/to/masked.fa}}`

- Chain output for liftOver-style coordinate mapping:

`bcftools consensus {{[-f|--fasta-ref]}} {{path/to/reference.fa}} {{[-c|--chain]}} {{path/to/output.chain}} {{path/to/variants.vcf.gz}} > {{path/to/consensus.fa}}`

- Restrict consensus generation to a region:

`bcftools consensus {{[-f|--fasta-ref]}} {{path/to/reference.fa}} {{[-r|--regions]}} {{chr:start-end}} {{path/to/variants.vcf.gz}} > {{path/to/region.fa}}`

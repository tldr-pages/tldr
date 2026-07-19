# bcftools call

> SNP/indel calling from genotype likelihoods.
> See also: `bcftools`, `bcftools mpileup`.
> More information: <https://samtools.github.io/bcftools/bcftools.html#call>.

- Call variants from a BCF/VCF with genotype likelihoods using the multiallelic caller:

`bcftools call {{[-m|--multiallelic-caller]}} {{path/to/input.bcf}} {{[-o|--output]}} {{path/to/output.vcf}}`

- Call and keep only variant sites:

`bcftools call {{[-m|--multiallelic-caller]}} {{[-v|--variants-only]}} {{path/to/input.bcf}} {{[-Oz|--output-type]}} z {{[-o|--output]}} {{path/to/calls.vcf.gz}}`

- Call variants from `mpileup` output streamed on `stdin`:

`bcftools mpileup {{[-f|--fasta-ref]}} {{path/to/reference.fa}} {{path/to/alignments.bam}} | bcftools call {{[-m|--multiallelic-caller]}} {{[-v|--variants-only]}} {{[-Oz|--output-type]}} z {{[-o|--output]}} {{path/to/calls.vcf.gz}}`

- Call variants for a specific region:

`bcftools call {{[-m|--multiallelic-caller]}} {{[-r|--regions]}} {{chr:start-end}} {{path/to/input.bcf}} {{[-o|--output]}} {{path/to/region.vcf}}`

- Output compressed BCF and write an index:

`bcftools call {{[-m|--multiallelic-caller]}} {{path/to/input.bcf}} {{[-Ob|--output-type]}} b {{[-o|--output]}} {{path/to/calls.bcf}} {{[-W|--write-index]}}`

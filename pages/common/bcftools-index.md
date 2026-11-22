# bcftools index

> Index bgzip-compressed VCF and BCF files for fast random access.
> See also: `bcftools`, `tabix`.
> More information: <https://samtools.github.io/bcftools/bcftools.html#index>.

- Create a CSI index (`.csi`) for a compressed VCF or BCF file:

`bcftools index {{path/to/input.vcf.gz}}`

- Create a TBI index (`.tbi`) for a compressed VCF file:

`bcftools index {{[-t|--tbi]}} {{path/to/input.vcf.gz}}`

- Overwrite an existing index:

`bcftools index {{[-f|--force]}} {{path/to/input.vcf.gz}}`

- Write the index to a specific file:

`bcftools index {{[-o|--output]}} {{path/to/index.csi}} {{path/to/input.vcf.gz}}`

- Print the number of records per contig using an existing index:

`bcftools index {{[-s|--stats]}} {{path/to/input.vcf.gz}}`

- Print the total number of records using an existing index:

`bcftools index {{[-n|--nrecords]}} {{path/to/input.vcf.gz}}`

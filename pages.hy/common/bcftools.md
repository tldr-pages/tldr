# bcftools

> VCF և BCF ֆայլերը շահարկելու գործիքներ:.
> Լրացուցիչ տեղեկություններ. <https://samtools.github.io/bcftools/bcftools.html>:.

- Դիտեք BCF ֆայլը և փոխարկեք [v]CF-ի `stdout`-ում:

`bcftools view {{path/to/input.bcf}} {{[-O|--output-type]}} v`

- Տեսակավորել VCF ֆայլի տարբերակները ըստ քրոմոսոմի և դիրքի, ելք բերել [b]CF ֆայլ և ինդեքսավորել տեսակավորված ելքը.:

`bcftools sort {{path/to/input.vcf.gz}} {{[-O|--output-type]}} b {{[-o|--output]}} {{path/to/sorted.bcf}} {{[-W|--write-index]}}`

- Միացնել տեսակավորված VCF ֆայլերը, որոնք կիսում են նույն նմուշները [z]ipped VCF-ին `stdout`-ում:

`bcftools concat {{path/to/chr1.vcf.gz path/to/chr2.vcf.gz ...}} {{[-O|--output-type]}} z`

- Զտել ցածր որակի տարբերակների համար և նշել «LowQual» պիտակը FILTER սյունակում.:

`bcftools filter {{[-e|--exclude]}} 'QUAL<20' {{[-s|--soft-filter]}} LowQual {{path/to/input.vcf.gz}}`

- Ավելացրեք ծանոթագրված սյունակներ ներդիրներով ինդեքսավորված աղյուսակից `stdout`-ում:

`bcftools annotate {{[-a|--annotations]}} {{path/to/annotations.tsv.gz}} {{[-c|--columns]}} CHROM,POS,REF,ALT,INFO/AF {{path/to/input.vcf.gz}}`

- Արդյունք [i]nter[sec]tion VCF ֆայլերի միջև՝ օգտագործելով 4 թելեր.:

`bcftools isec {{path/to/a.vcf.gz path/to/b.vcf.gz ...}} --threads 4 {{[-o|--output]}} {{path/to/intersection.vcf}}`

- Միավորել չհամընկնող նմուշները VCF ֆայլերից առանց ինդեքսների `stdout`-ում:

`bcftools merge {{path/to/cohort1.vcf.gz}} {{path/to/cohort2.vcf.gz}} --no-index`

- Ստեղծեք ինդեքս bgzipped VCF ֆայլի համար.:

`bcftools index {{path/to/input.vcf.gz}}`

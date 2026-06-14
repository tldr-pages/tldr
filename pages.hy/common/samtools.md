# samtools

> Գործիքներ բարձր թողունակության հաջորդականության (գենոմիկայի) տվյալների մշակման համար:.
> Օգտագործվում է SAM/BAM/CRAM ձևաչափով տվյալների ընթերցման/գրման/խմբագրման/ինդեքսավորման/դիտման համար:.
> Լրացուցիչ տեղեկություններ. <https://www.htslib.org/doc/samtools.html>:.

- Փոխարկեք SAM մուտքագրված ֆայլը BAM հոսքի և պահեք ֆայլում.:

`samtools view -S {{[-b|--bam]}} {{input.sam}} > {{output.bam}}`

- Մուտքագրեք `stdin`-ից (-) և տպեք SAM-ի վերնագիրը և որոշակի շրջանի վրա համընկնող ցանկացած ընթերցում `stdout`-ում:

`{{other_command}} | samtools view {{[-h|--with-header]}} - chromosome:start-end`

- Տեսակավորել ֆայլը և պահել BAM-ում (ելքային ձևաչափը ավտոմատ կերպով որոշվում է ելքային ֆայլի ընդլայնումից).:

`samtools sort {{input}} {{[-o|--output]}} {{output.bam}}`

- Ինդեքսավորեք տեսակավորված BAM ֆայլը (ստեղծում է `sorted_input.bam.bai`):

`samtools index {{sorted_input.bam}}`

- Տպել հավասարեցման վիճակագրությունը ֆայլի վերաբերյալ.:

`samtools flagstat {{sorted_input}}`

- Հաշվեք հավասարեցումները յուրաքանչյուր ինդեքսի համար (քրոմոսոմ/կոնտիգ).:

`samtools idxstats {{sorted_indexed_input}}`

- Միավորել բազմաթիվ ֆայլեր.:

`samtools merge {{output}} {{input1 input2 ...}}`

- Մուտքային ֆայլը բաժանել ըստ ընթերցված խմբերի.:

`samtools split {{merged_input}}`

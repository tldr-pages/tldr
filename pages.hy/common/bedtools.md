# մահճակալի գործիքներ

> Գենոմատիկ անալիզի առաջադրանքների համար նախատեսված գործիքների շվեյցարական բանակային դանակ:.
> Օգտագործվում է BAM, BED, GFF/GTF, VCF ձևաչափով տվյալները հատելու, խմբավորելու, փոխակերպելու և հաշվելու համար:.
> Լրացուցիչ տեղեկություններ. <https://bedtools.readthedocs.io/en/latest/content/overview.html#summary-of-available-tools>:.

- Հատեք [a] ֆայլը և ֆայլ(ներ)ը [b] հաջորդականությունների [s]trand-ի հետ կապված և արդյունքը պահպանեք որոշակի ֆայլում.:

`bedtools intersect -a {{path/to/file_A}} -b {{path/to/file_B1 path/to/file_B2 ...}} -s > {{path/to/output_file}}`

- Երկու ֆայլ հատեք [l]eft [o]uter [j]oin-ով, այսինքն՝ զեկուցեք յուրաքանչյուր հատկանիշի `file1`-ից և NULL-ից, եթե չհամընկնի `file2`-ի հետ:

`bedtools intersect -a {{path/to/file1}} -b {{path/to/file2}} -loj > {{path/to/output_file}}`

- Օգտագործեք ավելի արդյունավետ ալգորիթմ՝ երկու նախապես դասավորված ֆայլերը հատելու համար.:

`bedtools intersect -a {{path/to/file1}} -b {{path/to/file2}} -sorted > {{path/to/output_file}}`

- [g]խմբավորեք ֆայլը՝ հիմնված առաջին երեք և հինգերորդ [c] սյունակի վրա և կիրառեք գումարի [o] գործողությունը վեցերորդ սյունակում.:

`bedtools groupby -i {{path/to/file}} -c 1-3,5 -g 6 -o sum`

- Փոխարկել bam ֆորմատավորված [i]nput ֆայլը մահճակալի ձևաչափով.:

`bedtools bamtobed -i {{path/to/file.bam}} > {{path/to/file.bed}}`

- Գտեք `file1.bed`-ի բոլոր հատկանիշների համար ամենամոտը՝ `file2.bed`-ում և գրեք դրանց [d] հեռավորությունը լրացուցիչ սյունակում (մուտքագրված ֆայլերը պետք է տեսակավորվեն).:

`bedtools closest -a {{path/to/file1.bed}} -b {{path/to/file2.bed}} -d`

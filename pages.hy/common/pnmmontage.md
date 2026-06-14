# pnmմոնտաժ

> Ստեղծեք մոնտաժ մի քանի PNM պատկերներից:.
> More information: <https://netpbm.sourceforge.net/doc/pnmmontage.html>.

- Ստեղծեք նշված պատկերների փաթեթավորում.:

`pnmmontage {{path/to/image1.pnm path/to/image2.pnm ...}} > {{path/to/output.pnm}}`

- Նշեք փաթեթավորման որակը (Նշում. ավելի մեծ արժեքները արտադրում են ավելի փոքր փաթեթավորումներ, բայց ավելի երկար է պահանջվում՝ հաշվարկելու համար):

`pnmmontage -{{0..9}} {{path/to/image1.pnm path/to/image2.pnm ...}} > {{path/to/output.pnm}}`

- Արտադրեք փաթեթավորում, որը չի գերազանցում օպտիմալ փաթեթավորման `p` տոկոսը.:

`pnmmontage {{[-qua|-quality]}} {{p}} {{path/to/image1.pnm path/to/image2.pnm ...}} > {{path/to/output.pnm}}`

- Փաթեթավորված պատկերի մեջ մուտքագրված ֆայլերի դիրքերը գրեք մեքենայական ընթեռնելի ֆայլում՝:

`pnmmontage {{[-d|-data]}} {{path/to/datafile}} {{path/to/image1.pnm path/to/image2.pnm ...}} > {{path/to/output.pnm}}`

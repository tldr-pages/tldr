# pgmhist

> Տպեք PGM պատկերում առկա արժեքների հիստոգրամը:.
> Տես նաև՝ `ppmhist`:.
> Լրացուցիչ տեղեկություններ. <https://netpbm.sourceforge.net/doc/pgmhist.html>:.

- Ցուցադրել հիստոգրամը մարդու ընթերցման համար.:

`pgmhist {{path/to/image.pgm}}`

- Ցուցադրել միջին մոխրագույն արժեքը.:

`pgmhist {{[-me|-median]}} {{path/to/image.pgm}}`

- Ցուցադրել չորս քառորդ մոխրագույն արժեքը.:

`pgmhist {{[-qua|-quartile]}} {{path/to/image.pgm}}`

- Հաղորդել անվավեր մոխրագույն արժեքների առկայության մասին.:

`pgmhist {{[-f|-forensic]}} {{path/to/image.pgm}}`

- Ցուցադրել մեքենանընթեռնելի արդյունքը.:

`pgmhist {{[-ma|-machine]}} {{path/to/image.pgm}}`

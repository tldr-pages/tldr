# pbmtext

> Տեքստը ներկայացրեք որպես PBM պատկեր:.
> Տես նաև՝ `pbmtextps`:.
> Լրացուցիչ տեղեկություններ. <https://netpbm.sourceforge.net/doc/pbmtext.html>:.

- Տեքստի մեկ տող ներկայացրեք որպես PBM պատկեր.:

`pbmtext "{{Hello World!}}" > {{path/to/output.pbm}}`

- Ներկայացրեք տեքստի մի քանի տող որպես PBM պատկեր.:

`echo "{{Hello\nWorld!}}" | pbmtext > {{path/to/output.pbm}}`

- Տեքստը մատուցեք՝ օգտագործելով հատուկ տառատեսակ, որը տրամադրվում է որպես PBM ֆայլ.:

`pbmtext {{[-f|-font]}} {{path/to/font.pbm}} "{{Hello World!}}" > {{path/to/output.pbm}}`

- Նշեք պիքսելների քանակը նիշերի և տողերի միջև.:

`echo "{{Hello\nWorld!}}" | pbmtext {{[-s|-space]}} {{3}} {{[-ls|-lspace]}} {{10}} > {{path/to/output.pbm}}`

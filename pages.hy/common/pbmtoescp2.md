# pbmtoescp2

> Փոխարկել PBM պատկերը ESC/P2 տպիչի ֆայլի:.
> Տես նաև՝ `pbmtoepson`, `escp2topbm`:.
> Լրացուցիչ տեղեկություններ. <https://netpbm.sourceforge.net/doc/pbmtoescp2.html>:.

- Փոխարկել PBM պատկերը ESC/P2 տպիչի ֆայլի.:

`pbmtoescp2 {{path/to/image.pbm}} > {{path/to/output.escp2}}`

- Նշեք ելքի սեղմումը.:

`pbmtoescp2 {{[-c|-compression]}} {{0|1}} {{path/to/image.pbm}} > {{path/to/output.escp2}}`

- Նշեք ելքի հորիզոնական և ուղղահայաց լուծաչափը մեկ դյույմի համար նախատեսված կետերով.:

`pbmtoescp2 {{[-re|-resolution]}} {{180|360|720}} {{path/to/image.pbm}} > {{path/to/output.escp2}}`

- Տեղադրեք formfeed հրամանը ելքի վերջում.:

`pbmtoescp2 {{[-f|-formfeed]}} {{path/to/image.pbm}} > {{path/to/output.escp2}}`

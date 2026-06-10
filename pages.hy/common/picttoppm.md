# picttoppm

> Վերափոխեք Macintosh PICT ֆայլը PPM պատկերի:.
> Լրացուցիչ տեղեկություններ. <https://netpbm.sourceforge.net/doc/picttoppm.html>:.

- Փոխակերպեք PICT ֆայլը PPM պատկերի.:

`picttoppm {{path/to/file.pict}} > {{path/to/file.ppm}}`

- Ստիպեք PICT ֆայլի ցանկացած պատկեր թողարկվել ամբողջական լուծաչափով.:

`picttoppm {{[-fu|-fullres]}} {{path/to/file.pict}} > {{path/to/file.ppm}}`

- Մի ենթադրեք, որ մուտքագրված ֆայլը պարունակում է PICT վերնագիր և կատարեք միայն արագ նկարման գործողություններ.:

`picttoppm {{[-n|-noheader]}} {{[-quic|-quickdraw]}} {{path/to/file.pict}} > {{path/to/file.ppm}}`

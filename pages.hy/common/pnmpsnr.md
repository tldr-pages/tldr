# pnmpsnr

> Հաշվեք երկու պատկերների տարբերությունը:.
> Լրացուցիչ տեղեկություններ. <https://netpbm.sourceforge.net/doc/pnmpsnr.html>:.

- Հաշվեք տարբերությունը, այսինքն՝ գագաթնակետային ազդանշան-աղմուկ հարաբերակցությունը (PSNR) երկու պատկերների միջև.:

`pnmpsnr {{path/to/file1.pnm}} {{path/to/file2.pnm}}`

- Համեմատեք գունային բաղադրիչները, այլ ոչ թե պատկերների պայծառությունն ու քրոմինությունը.:

`pnmpsnr {{path/to/file1.pnm}} {{path/to/file2.pnm}} -rgb`

- Աշխատեք համեմատության ռեժիմում, այսինքն՝ թողարկեք միայն `nomatch` կամ `match`՝ կախված նրանից, թե արդյոք հաշվողական PSNR-ը գերազանցում է `n`-ը, թե ոչ:

`pnmpsnr {{path/to/file1.pnm}} {{path/to/file2.pnm}} -target {{n}}`

- Գործարկեք համեմատության ռեժիմով և համեմատեք պատկերի առանձին բաղադրիչները, այսինքն՝ Y, Cb և Cr, համապատասխան շեմերին.:

`pnmpsnr {{path/to/file1.pnm}} {{path/to/file2.pnm}} -target1 {{threshold_Y}} -target2 {{threshold_Cb}} -target3 {{threshold_Cr}}`

- Գործարկեք համեմատության ռեժիմով և համեմատեք պատկերի առանձին բաղադրիչները, այսինքն՝ կարմիր, կանաչ և կապույտը համապատասխան շեմերին.:

`pnmpsnr {{path/to/file1.pnm}} {{path/to/file2.pnm}} -rgb -target1 {{threshold_red}} -target2 {{threshold_green}} -target3 {{threshold_blue}}`

- Արտադրել մեքենանընթեռնելի արդյունք.:

`pnmpsnr {{path/to/file1.pnm}} {{path/to/file2.pnm}} -machine`

# կախարդական մոնտաժ

> Կղմինդր պատկերները հարմարեցված ցանցի մեջ:.
> Տես նաև՝ `magick`:.
> Լրացուցիչ տեղեկություններ. <https://imagemagick.org/script/montage.php>:.

- Պատկերները տեղադրեք ցանցի մեջ՝ ավտոմատ կերպով փոխելով պատկերները ցանցի բջիջի չափից ավելի մեծ:

`magick montage {{path/to/image1.jpg path/to/image2.jpg ...}} {{path/to/montage.jpg}}`

- Պատկերները տեղադրեք ցանցի մեջ՝ ավտոմատ կերպով հաշվարկելով ցանցի բջիջի չափը ամենամեծ պատկերից.:

`magick montage {{path/to/image1.jpg path/to/image2.jpg ...}} -geometry {{+0+0}} {{path/to/montage.jpg}}`

- Նշեք ցանցի բջիջի չափը և չափափոխեք պատկերները, որպեսզի դրանք համապատասխանեն սալիկապատելուց առաջ:

`magick montage {{path/to/image1.jpg path/to/image2.jpg ...}} -geometry {{640x480+0+0}} {{path/to/montage.jpg}}`

- Սահմանափակեք ցանցում տողերի և սյունակների քանակը՝ պատճառ դառնալով, որ մուտքային պատկերները լցվեն բազմաթիվ ելքային մոնտաժների մեջ.:

`magick montage {{path/to/image1.jpg path/to/image2.jpg ...}} -geometry {{+0+0}} -tile {{2x3}} {{montage_%d.jpg}}`

- Չափափոխեք և կտրեք պատկերները՝ նախքան սալիկապատելը իրենց ցանցային բջիջները լրացնելու համար.:

`magick montage {{path/to/image1.jpg path/to/image2.jpg ...}} -geometry {{+0+0}} -resize {{640x480^}} -gravity {{center}} -crop {{640x480+0+0}} {{path/to/montage.jpg}}`

# կախարդական համեմատություն

> Ստեղծեք համեմատական պատկեր՝ երկու պատկերների միջև տարբերությունը տեսողականորեն նշելու համար:.
> Տես նաև՝ `magick`:.
> Լրացուցիչ տեղեկություններ. <https://imagemagick.org/script/compare.php>:.

- Համեմատեք երկու պատկեր.:

`magick compare {{path/to/image1.png}} {{path/to/image2.png}} {{path/to/diff.png}}`

- Համեմատեք երկու պատկերներ՝ օգտագործելով նշված չափանիշը.:

`magick compare -verbose -metric {{PSNR}} {{path/to/image1.png}} {{path/to/image2.png}} {{path/to/diff.png}}`

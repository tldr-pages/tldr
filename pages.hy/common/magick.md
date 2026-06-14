#կախարդություն

> Ստեղծեք, խմբագրեք, կազմեք կամ փոխարկեք պատկերի ձևաչափերի միջև:.
> Այս գործիքը փոխարինում է `convert`-ին ImageMagick 7+-ում: Տես `magick convert`՝ հին գործիքը 7+ տարբերակներում օգտագործելու համար:.
> Որոշ ենթահրամաններ, ինչպիսիք են `mogrify`-ն, ունեն իրենց օգտագործման փաստաթղթերը:.
> Լրացուցիչ տեղեկություններ. <https://imagemagick.org/script/magick.php>:.

- Փոխարկել պատկերի ձևաչափերի միջև.:

`magick {{path/to/input_image.png}} {{path/to/output_image.jpg}}`

- Չափափոխել պատկերը, ստեղծելով նոր պատճեն.:

`magick {{path/to/input_image.jpg}} -resize {{100x100}} {{path/to/output_image.jpg}}`

- Չափափոխել պատկերը տոկոսով.:

`magick {{path/to/input_image.png}} -resize {{50}}% {{path/to/output_image.png}}`

- Սանդղակավորեք պատկերը, որպեսզի ունենա ֆայլի սահմանված չափ.:

`magick {{path/to/input_image.png}} -define jpeg:extent={{512kb}} {{path/to/output_image.jpg}}`

- Ստեղծեք GIF բոլոր JPEG պատկերներից ընթացիկ գրացուցակում.:

`magick {{*.jpg}} {{path/to/images.gif}}`

- Ստեղծեք շաշկի ձևանմուշ.:

`magick -size {{640x480}} pattern:checkerboard {{path/to/checkerboard.png}}`

- Ստեղծեք PDF ֆայլ ընթացիկ գրացուցակի բոլոր JPEG պատկերներից.:

`magick {{*.jpg}} -adjoin {{path/to/file.pdf}}`

# magick փոխակերպում

> Փոխակերպեք պատկերների ձևաչափերի միջև, չափեք, միացեք և ստեղծեք պատկերներ և շատ ավելին:.
> Նշում․ այս գործիքը (նախկինում՝ `convert`) փոխարինվել է `magick`-ով ImageMagick 7+-ում:.
> Լրացուցիչ տեղեկություններ. <https://imagemagick.org/script/convert.php>:.

- Փոխակերպեք պատկերը JPEG-ից PNG-ի.:

`magick convert {{path/to/input_image.jpg}} {{path/to/output_image.png}}`

- Պատկերը չափեք իր սկզբնական չափի 50%-ով.:

`magick convert {{path/to/input_image.png}} -resize 50% {{path/to/output_image.png}}`

- Սանդղակավորեք պատկերը՝ պահպանելով բնօրինակի հարաբերակցությունը մինչև 640x480 առավելագույն չափս:

`magick convert {{path/to/input_image.png}} -resize 640x480 {{path/to/output_image.png}}`

- Սանդղակավորեք պատկերը, որպեսզի ունենա ֆայլի սահմանված չափ.:

`magick convert {{path/to/input_image.png}} -define jpeg:extent={{512kb}} {{path/to/output_image.jpg}}`

- Ուղղահայաց/հորիզոնական կերպով կցեք պատկերները և թողեք դատարկ տարածքը թափանցիկ.:

`magick convert -background none {{path/to/image1.png path/to/image2.png ...}} {{-append|+append}} {{path/to/output_image.png}}`

- Ստեղծեք GIF մի շարք պատկերներից, որոնց միջև 100 մս ուշացումով:

`magick convert {{path/to/image1.png path/to/image2.png ...}} -delay {{10}} {{path/to/animation.gif}}`

- Ստեղծեք պատկեր, բացի պինդ կարմիր ֆոնից.:

`magick convert -size {{800x600}} "xc:{{#ff0000}}" {{path/to/image.png}}`

- Ստեղծեք ֆավիկոն տարբեր չափերի մի քանի պատկերներից.:

`magick convert {{path/to/image1.png path/to/image2.png ...}} {{path/to/favicon.ico}}`

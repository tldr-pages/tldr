# ppmfade

> Ստեղծեք անցում երկու PPM պատկերների միջև:.
> Լրացուցիչ տեղեկություններ. <https://netpbm.sourceforge.net/doc/ppmfade.html>:.

- Ստեղծեք անցում երկու PPM պատկերների միջև ([f]առաջին և [l]վերջին)՝ օգտագործելով նշված էֆեկտը.:

`ppmfade -f {{path/to/image1.ppm}} -l {{path/to/image2.ppm}} -{{mix|spread|shift|relief|oil|...}}`

- Ստեղծեք անցում, որը սկսվում է նշված պատկերով և ավարտվում պինդ սև պատկերով.:

`ppmfade -f {{path/to/image.ppm}} -{{mix|spread|shift|relief|oil|...}}`

- Ստեղծեք անցում, որը սկսվում է պինդ սև պատկերով և ավարտվում նշված պատկերով.:

`ppmfade -l {{path/to/image.ppm}} -{{mix|spread|shift|relief|oil|...}}`

- Ստացված պատկերները պահեք `base.NNNN.ppm` անունով ֆայլերում, որտեղ `NNNN` աճող թիվ է:

`ppmfade -f {{path/to/image1.ppm}} -l {{path/to/image2.ppm}} -{{mix|spread|shift|relief|oil|...}} -base {{base}}`

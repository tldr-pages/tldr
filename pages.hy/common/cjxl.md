# cjxl

> Սեղմել պատկերները JPEG XL-ով:.
> Ընդունված մուտքային ընդլայնումներն են՝ PNG, APNG, GIF, JPEG, EXR, PPM, PFM, PAM, PGX և JXL:.
> Լրացուցիչ տեղեկություններ. <https://github.com/libjxl/libjxl/blob/main/doc/man/cjxl.txt>:.

- Փոխարկել պատկերը JPEG XL:

`cjxl {{path/to/image.ext}} {{path/to/output.jxl}}`

- Սահմանեք որակը առանց կորուստների և առավելագույնի հասցրեք ստացված պատկերի սեղմումը.:

`cjxl --distance 0 --effort 9 {{path/to/image.ext}} {{path/to/output.jxl}}`

- Ցուցադրել չափազանց մանրամասն օգնություն.:

`cjxl {{[-h -v -v -v -v|--help --verbose --verbose --verbose --verbose]}}`

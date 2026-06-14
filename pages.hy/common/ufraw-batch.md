# ufraw-խմբաքանակ

> Փոխարկեք RAW ֆայլերը տեսախցիկներից ստանդարտ պատկերային ֆայլերի:.
> Լրացուցիչ տեղեկություններ. <https://manned.org/ufraw-batch>:.

- Պարզապես փոխարկեք RAW ֆայլերը JPEG-ի.:

`ufraw-batch --out-type=jpg {{input_file(s)}}`

- Պարզապես փոխարկեք RAW ֆայլերը PNG-ի.:

`ufraw-batch --out-type=png {{input_file(s)}}`

- Նախադիտման պատկերը հանեք չմշակված ֆայլից.:

`ufraw-batch --embedded-image {{input_file(s)}}`

- Պահպանեք ֆայլը մինչև տրված առավելագույնները MAX1 և MAX2:

`ufraw-batch --size=MAX1,MAX2 {{input_file(s)}}`

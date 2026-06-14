# ppmdither

> Կրճատեք պատկերի գույների քանակը՝ կիրառելով շեղումներ:.
> Լրացուցիչ տեղեկություններ. <https://netpbm.sourceforge.net/doc/ppmdither.html>:.

- Կարդացեք PPM պատկերը, կիրառեք dithering և պահեք այն ֆայլում.:

`ppmdither {{path/to/image.ppm}} > {{path/to/file.ppm}}`

- Յուրաքանչյուր հիմնական գույնի համար նշեք երանգների ցանկալի քանակը.:

`ppmdither {{[-r|-red]}} {{2}} {{[-g|-green]}} {{3}} {{[-b|-blue]}} {{2}} {{path/to/image.ppm}} > {{path/to/file.ppm}}`

- Նշեք շեղող մատրիցայի չափերը.:

`ppmdither {{[-d|-dim]}} {{2}} {{path/to/image.ppm}} > {{path/to/file.ppm}}`

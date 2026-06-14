# palmtopnm

> Փոխարկել Palm bitmap ֆայլը PNM պատկերի:.
> Լրացուցիչ տեղեկություններ. <https://netpbm.sourceforge.net/doc/palmtopnm.html>:.

- Փոխակերպեք Palm bitmap-ը PNM պատկերի.:

`palmtopnm {{path/to/file.palm}} > {{path/to/file.pnm}}`

- Ցուցադրել մուտքագրված ֆայլի մասին տեղեկատվություն.:

`palmtopnm {{[-verb|-verbose]}} {{path/to/file.palm}} > {{path/to/file.pnm}}`

- Փոխակերպեք մուտքային ֆայլում պարունակվող պատկերի n'-րդ կատարումը.:

`palmtopnm {{[-r|-rendition]}} {{n}} {{path/to/file.palm}} > {{path/to/file.pnm}}`

- Մուտքային ֆայլի գույների հիստոգրամը գրեք `stdout`:

`palmtopnm {{[-s|-showhist]}} {{path/to/file.palm}} > {{path/to/file.pnm}}`

- Արտադրեք մուտքային պատկերի թափանցիկ գույնը, եթե սահմանված է.:

`palmtopnm {{[-t|-transparent]}} {{path/to/file.palm}}`

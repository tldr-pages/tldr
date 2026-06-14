# pnmalias

> Կիրառել հակաալիզինգը PNM պատկերի վրա:.
> Լրացուցիչ տեղեկություններ. <https://netpbm.sourceforge.net/doc/pnmalias.html>:.

- Կատարեք հակաալիզինգ PNM պատկերի վրա՝ վերցնելով սև պիքսելները որպես ֆոն և սպիտակ պիքսելները որպես առաջին պլան:

`pnmalias {{path/to/input.pnm}} > {{path/to/output.ppm}}`

- Հստակորեն նշեք ֆոնի և առաջին պլանի գույնը.:

`pnmalias -bcolor {{background_color}} -fcolor {{foreground_color}} {{path/to/input.pnm}} > {{path/to/output.ppm}}`

- Կիրառել altialiasing միայն առաջին պլանի պիքսելների վրա.:

`pnmalias {{[-fo|-fonly]}} {{path/to/input.pnm}} > {{path/to/output.ppm}}`

- Կիրառեք հակաալիզինգ ֆոնային պիքսելների բոլոր շրջապատող պիքսելներին.:

`pnmalias {{[-ba|-balias]}} {{path/to/input.pnm}} > {{path/to/output.ppm}}`

# pnmcolormap

> Ստեղծեք քվանտացման գունային քարտեզ PNM պատկերի համար:.
> Լրացուցիչ տեղեկություններ. <https://netpbm.sourceforge.net/doc/pnmcolormap.html>:.

- Ստեղծեք պատկեր՝ օգտագործելով միայն `n_colors` կամ ավելի քիչ գույներ, որքան հնարավոր է մոտ մուտքագրված պատկերին:

`pnmcolormap {{n_colors}} {{path/to/input.pnm}} > {{path/to/output.ppm}}`

- Օգտագործեք splitspread ռազմավարությունը ելքային գույները որոշելու համար, հնարավոր է ավելի լավ արդյունք տալ փոքր մանրամասներով պատկերների համար.:

`pnmcolormap {{[-splits|-splitspread]}} {{n_colors}} {{path/to/input.pnm}} > {{path/to/output.ppm}}`

- Տեսակավորեք ստացված գունային քարտեզը, որն օգտակար է գունային քարտեզները համեմատելու համար.:

`pnmcolormap {{[-so|-sort]}} {{path/to/input.pnm}} > {{path/to/output.ppm}}`

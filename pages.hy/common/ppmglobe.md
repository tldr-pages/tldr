# ppmglobe

> Ստեղծեք պատկերի շերտեր, որոնք հարմար են գնդակի վրա սոսնձվելու համար:.
> Տես նաև՝ `pnmmercator`:.
> Լրացուցիչ տեղեկություններ. <https://netpbm.sourceforge.net/doc/ppmglobe.html>:.

- Փոխակերպեք պատկերը շերտերի, որոնք կարող են կտրվել և սոսնձվել գնդիկի վրա.:

`ppmglobe {{number_of_strips}} {{path/to/image.ppm}} > {{path/to/output.ppm}}`

- Օգտագործեք նշված գույնը շերտերի միջև ընկած հատվածների համար.:

`ppmglobe {{[-b|-background]}} {{red}} {{number_of_strips}} {{path/to/image.ppm}} > {{path/to/output.ppm}}`

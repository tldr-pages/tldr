# pamundice

> Միավորել Netpbm պատկերների ցանցը մեկի մեջ:.
> Տես նաև՝ `pamdice`:.
> Լրացուցիչ տեղեկություններ. <https://netpbm.sourceforge.net/doc/pamundice.html>:.

- Միավորել պատկերները, որոնց անունները համապատասխանում են `printf` ոճի ֆայլի անվան արտահայտությանը: Ենթադրենք որոշակի չափի ցանց.:

`pamundice {{filename_%1d_%1a.ppm}} {{[-a|-across]}} {{grid_width}} {{[-d|-down]}} {{grid_height}} > {{path/to/output.ppm}}`

- Ենթադրենք, որ սալիկները հորիզոնական և ուղղահայաց համընկնում են նշված քանակով.:

`pamundice {{filename_%1d_%1a.ppm}} {{[-a|-across]}} {{x_value}} {{[-d|-down]}} {{y_value}} {{[-ho|-hoverlap]}} {{value}} {{[-vo|-voverlap]}} {{value}} > {{path/to/output.ppm}}`

- Նշեք պատկերները, որոնք պետք է համակցվեն մեկ տողում մեկ ֆայլի անուն պարունակող տեքստային ֆայլի միջոցով.:

`pamundice {{[-l|-listfile]}} {{path/to/file.txt}} {{[-a|-across]}} {{x_value}} {{[-d|-down]}} {{y_value}} > {{path/to/output.ppm}}`

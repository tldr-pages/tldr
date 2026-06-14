# pnmrotate

> Պտտեցնել PNM պատկերը:.
> Լրացուցիչ տեղեկություններ. <https://netpbm.sourceforge.net/doc/pnmrotate.html>:.

- Պտտեցնել PNM պատկերը որոշ անկյան տակ (չափված աստիճաններով, ժամացույցի սլաքի հակառակ ուղղությամբ).:

`pnmrotate {{angle}} {{path/to/input.pnm}} > {{path/to/output.pnm}}`

- Նշեք ֆոնի գույնը, որը բացահայտվում է մուտքագրված պատկերը պտտելով.:

`pnmrotate {{[-b|-background]}} {{color}} {{angle}} {{path/to/input.pnm}} > {{path/to/output.pnm}}`

- Անջատեք հակաալիզինգը, բարելավում է կատարումը, բայց նվազեցնում որակը.:

`pnmrotate {{[-n|-noantialias]}} {{angle}} {{path/to/input.pnm}} > {{path/to/output.pnm}}`

#փնմթոսգի

> Փոխարկել PNM ֆայլը SGI պատկերի ֆայլի:.
> Լրացուցիչ տեղեկություններ. <https://netpbm.sourceforge.net/doc/pnmtosgi.html>:.

- Փոխակերպեք PNM պատկերը SGI պատկերի.:

`pnmtosgi {{path/to/input.pnm}} > {{path/to/output.sgi}}`

- Անջատել կամ միացնել սեղմումը.:

`pnmtosgi -{{verbatim|rle}} {{path/to/input.pnm}} > {{path/to/output.sgi}}`

- Նշված տողը գրեք SGI պատկերի վերնագրի `imagename` դաշտում.:

`pnmtosgi {{[-i|-imagename]}} {{string}} {{path/to/input.pnm}} > {{path/to/output.sgi}}`

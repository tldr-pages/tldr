# pnmconvol

> Խճճել PNM պատկերը:.
> Լրացուցիչ տեղեկություններ. <https://netpbm.sourceforge.net/doc/pnmconvol.html>:.

- Փաթաթել PNM պատկերը նշված ոլորման մատրիցով.:

`pnmconvol -matrix=-1,3,-1 {{path/to/image.pnm}} > {{path/to/output.pnm}}`

- Միավորել PNM պատկերը կոնվուլյացիոն մատրիցով նշված ֆայլերում, մուտքագրված պատկերի յուրաքանչյուր շերտի համար.:

`pnmconvol -matrixfile {{path/to/matrix1,path/to/matrix2,...}} {{path/to/image.pnm}} > {{path/to/output.pnm}}`

- Խճճել PNM պատկերը ոլորման մատրիցով նշված PNM ֆայլում.:

`pnmconvol {{path/to/matrix.pnm}} {{path/to/image.pnm}} > {{path/to/output.pnm}}`

- Նորմալացրեք կշիռները ոլորման մատրիցում այնպես, որ դրանք գումարվեն մեկին.:

`pnmconvol -matrix=-1,3,-1 -normalize {{path/to/image.pnm}} > {{path/to/output.pnm}}`

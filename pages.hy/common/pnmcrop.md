# pnmcrop

> Կտրել PNM պատկերները:.
> Լրացուցիչ տեղեկություններ. <https://netpbm.sourceforge.net/doc/pnmcrop.html>:.

- Հեռացրեք սպիտակ եզրագծերը PNM պատկերի վրա.:

`pnmcrop {{[-w|-white]}} {{path/to/image.pnm}} > {{path/to/output.pnm}}`

- Հեռացրեք նշված գույնի եզրագծերը, որոնք գտնվում են պատկերի վերևի և ձախ կողմում.:

`pnmcrop -bg-color {{color}} {{[-t|-top]}} {{[-l|-left]}} {{path/to/image.pnm}} > {{path/to/output.pnm}}`

- Որոշեք հեռացվող եզրագծերի գույնը նշված անկյունում գտնվող պիքսելի գույնով.:

`pnmcrop -bg-corner {{topleft|topright|bottomleft|bottomright}} {{path/to/image.pnm}} > {{path/to/output.pnm}}`

- Թողեք եզրագիծ `n` պիքսել լայնությամբ: Բացի այդ, նշեք վարքագիծը, եթե պատկերն ամբողջությամբ պատրաստված է ֆոնից.:

`pnmcrop {{[-m|-margin]}} {{n}} {{[-blan|-blank-image]}} {{pass|minimize|maxcrop}} {{path/to/image.pnm}} > {{path/to/output.pnm}}`

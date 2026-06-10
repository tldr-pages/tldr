# pnmhistmap

> Գծե՛ք PNM պատկերի հիստոգրամա:.
> Լրացուցիչ տեղեկություններ. <https://netpbm.sourceforge.net/doc/pnmhistmap.html>:.

- Նկարեք PNM պատկերի հիստոգրամ.:

`pnmhistmap {{path/to/input.pnm}} > {{path/to/output.pnm}}`

- Հիստոգրամը գծեք որպես կետեր՝ գծերի փոխարեն.:

`pnmhistmap {{[-d|-dots]}} {{path/to/input.pnm}} > {{path/to/output.pnm}}`

- Նշեք ինտենսիվության արժեքների շրջանակը, որը ներառում է.:

`pnmhistmap {{[-l|-lval]}} {{minval}} {{[-rv|-rval]}} {{maxval}} {{path/to/input.pnm}} > {{path/to/output.pnm}}`

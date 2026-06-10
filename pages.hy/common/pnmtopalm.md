# pnmtopalm

> Փոխարկել PNM պատկերը Palm bitmap-ի:.
> Լրացուցիչ տեղեկություններ. <https://netpbm.sourceforge.net/doc/pnmtopalm.html>:.

- Փոխակերպեք PNM պատկերը Palm bitmap-ի.:

`pnmtopalm {{path/to/file.pnm}} > {{path/to/file.palm}}`

- Նշեք ստացված bitmap-ի գույնի խորությունը.:

`pnmtopalm {{[-dep|-depth]}} {{1|2|4|8|16}} {{path/to/file.pnm}} > {{path/to/file.palm}}`

- Ստացված bitmap-ի համար ընտրեք սեղմման մեթոդ.:

`pnmtopalm -{{scanline_compression|rle_compression|packbits_compression}} {{path/to/file.pnm}} > {{path/to/file.palm}}`

- Կառուցեք հատուկ գունային քարտեզ և ներառեք այն ստացված bitmap-ում.:

`pnmtopalm {{[-c|-colormap]}} {{path/to/file.pnm}} > {{path/to/file.palm}}`

- Նշեք bitmap-ի խտությունը.:

`pnmtopalm {{[-den|-density]}} {{72|108|144|216|288}} {{path/to/file.pnm}} > {{path/to/file.palm}}`

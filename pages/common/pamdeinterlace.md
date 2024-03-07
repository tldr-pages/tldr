# pamdeinterlace

> Remove every other row in a Netpbm image.
> See also: `pammixinterlace`.
> More information: <https://netpbm.sourceforge.net/doc/pamdeinterlace.html>.

- Produce an image consisting of the input's even-numbered rows:

`pamdeinterlace {{path/to/image.ppm}} > {{path/to/output.ppm}}`

- Produce an image consisting of the input's odd-numbered rows:

`pamdeinterlace -takeodd {{path/to/image.ppm}} > {{path/to/output.ppm}}`

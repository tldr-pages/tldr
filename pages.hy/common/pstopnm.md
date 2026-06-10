# pstopnm

> Փոխակերպեք PostScript ֆայլը PNM պատկերի:.
> Լրացուցիչ տեղեկություններ. <https://netpbm.sourceforge.net/doc/pstopnm.html>:.

- Փոխակերպեք PS ֆայլը PNM պատկերների՝ մուտքագրման N էջը պահելով `path/to/fileN.ppm`-ի:

`pstopnm {{path/to/file.ps}}`

- Հստակորեն նշեք ելքային ձևաչափը.:

`pstopnm -{{pbm|pgm|ppm}} {{path/to/file.ps}}`

- Նշեք ելքի լուծումը մեկ դյույմի կետերով.:

`pstopnm -dpi {{n}} {{path/to/file.ps}}`

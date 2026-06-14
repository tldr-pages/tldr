# pbmclean

> Մաքրել PBM պատկերը՝ ջնջելով մեկուսացված սև և սպիտակ պիքսելները:.
> Լրացուցիչ տեղեկություններ. <https://netpbm.sourceforge.net/doc/pbmclean.html>:.

- Մաքրել PBM պատկերը՝ ջնջելով մեկուսացված սև և սպիտակ պիքսելները.:

`pbmclean {{path/to/image.pbm}} > {{path/to/output.pbm}}`

- Մաքրել միայն սև/սպիտակ պիքսելները.:

`pbmclean -{{black|white}} {{path/to/image.pbm}} > {{path/to/output.pbm}}`

- Նշեք նույն գույնի հարևան պիքսելների նվազագույն քանակը, որպեսզի պիքսելը մեկուսացված չհամարվի.:

`pbmclean {{[-m|-minneighbours]}} {{3}} {{path/to/image.pbm}} > {{path/to/output.pbm}}`

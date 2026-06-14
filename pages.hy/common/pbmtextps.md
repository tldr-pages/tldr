# pbmtextps

> Տեքստը մատուցեք որպես PBM պատկեր՝ օգտագործելով PostScript-ը:.
> Տես նաև՝ `pbmtext`:.
> Լրացուցիչ տեղեկություններ. <https://netpbm.sourceforge.net/doc/pbmtextps.html>:.

- Տեքստի մեկ տող ներկայացրեք որպես PBM պատկեր.:

`pbmtextps "{{Hello World!}}" > {{path/to/output.pbm}}`

- Նշեք տառատեսակը և տառաչափը.:

`pbmtextps -font {{Times-Roman}} -fontsize {{30}} "{{Hello World!}}" > {{path/to/output.pbm}}`

- Նշեք ցանկալի ձախ և վերին լուսանցքները.:

`pbmtextps {{[-l|-leftmargin]}} {{70}} {{[-t|-topmargin]}} {{162}} "{{Hello World!}}" > {{path/to/output.pbm}}`

- Արտադրված տեքստը մի թողարկեք որպես PBM պատկեր, այլ PostScript ծրագիր, որը կստեղծի այս պատկերը.:

`pbmtextps {{[-du|-dump-ps]}} "{{Hello World!}}" > {{path/to/output.ps}}`

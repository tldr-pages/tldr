# pbmtonokia

> Փոխարկեք PBM պատկերը Nokia-ի Smart Messaging ձևաչափերից մեկին:.
> Լրացուցիչ տեղեկություններ. <https://netpbm.sourceforge.net/doc/pbmtonokia.html>:.

- PBM պատկերը փոխարկեք Nokia օպերատորի լոգոյի՝ որպես hexcode:

`pbmtonokia {{[-f|-fmt]}} NEX_NOL -net {{network_operator_code}} {{path/to/image.pbm}} > {{path/to/output.hex}}`

- Փոխարկեք PBM պատկերը Nokia Group Graphic-ի որպես hexcode:

`pbmtonokia {{[-f|-fmt]}} NEX_NGG {{path/to/image.pbm}} > {{path/to/output.hex}}`

- PBM պատկերը փոխարկեք Nokia Picture Message-ի՝ նշված տեքստով որպես hexcode:

`pbmtonokia {{[-f|-fmt]}} NEX_NPM -txt {{text_message}} {{path/to/image.pbm}} > {{path/to/output.hex}}`

- Փոխակերպեք PBM պատկերը Nokia օպերատորի լոգոյի՝ որպես NOL ֆայլ.:

`pbmtonokia {{[-f|-fmt]}} NOL {{path/to/image.pbm}} > {{path/to/output.nol}}`

- Փոխակերպեք PBM պատկերը Nokia Group Graphic-ի որպես NGG ֆայլ.:

`pbmtonokia {{[-f|-fmt]}} NGG {{path/to/image.pbm}} > {{path/to/output.ngg}}`

- Փոխակերպեք PBM պատկերը Nokia Picture Message-ի որպես NPM ֆայլ.:

`pbmtonokia {{[-f|-fmt]}} NPM {{path/to/image.pbm}} > {{path/to/output.npm}}`

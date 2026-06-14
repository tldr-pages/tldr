# ppmcie

> Նկարեք CIE գունային աղյուսակը որպես PPM պատկեր:.
> Լրացուցիչ տեղեկություններ. <https://netpbm.sourceforge.net/doc/ppmcie.html>:.

- Նկարեք CIE գունային աղյուսակ՝ օգտագործելով REC709 գունային համակարգը որպես PPM պատկեր.:

`ppmcie > {{path/to/output.ppm}}`

- Նշեք օգտագործվող գունային համակարգը.:

`ppmcie -{{cie|ebu|hdtv|ntsc|smpte}} > {{path/to/output.ppm}}`

- Նշեք առանձին լուսատուների գտնվելու վայրը.:

`ppmcie -{{red|green|blue}} {{xpos ypos}} > {{path/to/output.ppm}}`

- Մի խոնարհեք Մաքսվելի եռանկյունուց դուրս գտնվող տարածքը.:

`ppmcie {{[-f|-full]}} > {{path/to/output.ppm}}`

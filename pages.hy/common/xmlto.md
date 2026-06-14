# xmlto

> Կիրառել XSL ոճի թերթիկ XML փաստաթղթում:.
> Լրացուցիչ տեղեկություններ. <https://manned.org/xmlto>:.

- Փոխակերպեք DocBook XML փաստաթուղթը PDF ձևաչափի.:

`xmlto pdf {{document.xml}}`

- Փոխակերպեք DocBook XML փաստաթուղթը HTML ձևաչափի և ստացված ֆայլերը պահեք առանձին գրացուցակում.:

`xmlto -o {{path/to/html_files}} html {{document.xml}}`

- Փոխակերպեք DocBook XML փաստաթուղթը մեկ HTML ֆայլի.:

`xmlto {{html-nochunks}} {{document.xml}}`

- Նշեք ոճաթերթ, որն օգտագործելու է DocBook XML փաստաթուղթը փոխարկելիս.:

`xmlto -x {{stylesheet.xsl}} {{output_format}} {{document.xml}}`

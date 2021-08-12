# xmlto

> Aplicați o foaie de stil XSL la un document XML.
> Mai multe informaţii: <https://pagure.io/xmlto>

- Conversia unui document DocBook XML în format PDF:

`xmlto {{pdf}} {{document.xml}}`

- Conversia unui document DocBook XML în format HTML și stocarea fișierelor rezultate într-un director separat:

`xmlto -o {{path/to/html_files}} {{html}} {{document.xml}}`

- Conversia unui document DocBook XML într-un singur fișier HTML:

`xmlto {{html-nochunks}} {{document.xml}}`

- Specificați o foaie de stil de utilizat în timpul conversiei unui document DocBook XML:

`xmlto -x {{stylesheet.xsl}} {{output_format}} {{document.xml}}`

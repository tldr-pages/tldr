# daps

> Բաց կոդով ծրագիր՝ DocBook XML-ը վերածելու ելքային ձևաչափերի, ինչպիսիք են HTML կամ PDF:.
> Լրացուցիչ տեղեկություններ. <https://opensuse.github.io/daps/doc/index.html>:.

- Ստուգեք, արդյոք DocBook XML ֆայլը վավեր է.:

`daps {{[-d|--docconfig]}} {{path/to/file.xml}} validate`

- Փոխակերպեք DocBook XML ֆայլը PDF.:

`daps {{[-d|--docconfig]}} {{path/to/file.xml}} pdf`

- Փոխակերպեք DocBook XML ֆայլը մեկ HTML ֆայլի.:

`daps {{[-d|--docconfig]}} {{path/to/file.xml}} html --single`

- Ցուցադրել օգնությունը.:

`daps {{[-h|--help]}}`

- Ցուցադրման տարբերակը:

`daps --version`

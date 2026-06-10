# xmllint

> XML վերլուծիչ և լինտեր, որն աջակցում է XPath-ին՝ XML ծառերը նավարկելու շարահյուսություն:.
> Լրացուցիչ տեղեկություններ. <https://manned.org/xmllint>:.

- Վերադարձրեք «foo» անունով բոլոր հանգույցները (պիտակները).:

`xmllint --xpath "//{{foo}}" {{source_file.xml}}`

- «foo» անունով առաջին հանգույցի բովանդակությունը վերադարձրեք որպես տող.:

`xmllint --xpath "string(//{{foo}})" {{source_file.xml}}`

- Վերադարձրեք HTML ֆայլում երկրորդ խարիսխի տարրի href հատկանիշը.:

`xmllint --html --xpath "string(//a[2]/@href)" webpage.xhtml`

- Ֆայլից վերադարձրեք մարդու համար ընթեռնելի (նեղված) XML-ը.:

`xmllint --format {{source_file.xml}}`

- Ստուգեք, որ XML ֆայլը համապատասխանում է իր DOCTYPE հռչակագրի պահանջներին.:

`xmllint --valid {{source_file.xml}}`

- Վավերացրեք XML-ը առցանց հյուրընկալված DTD սխեմայի դեմ.:

`xmllint --dtdvalid {{url}} {{source_file.xml}}`

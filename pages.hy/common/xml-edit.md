# xml խմբագրում

> Խմբագրել XML փաստաթուղթը:.
> Լրացուցիչ տեղեկություններ. <https://xmlstar.sourceforge.net/doc/UG/xmlstarlet-ug.html#idm47077139594320>:.

- Ջնջել XPATH-ին համապատասխանող տարրերը XML փաստաթղթից.:

`xml {{[ed|edit]}} {{[-d|--delete]}} "{{XPATH1}}" {{path/to/input.xml|uri}}`

- Տեղափոխեք XML փաստաթղթի տարրային հանգույցը XPATH1-ից XPATH2:

`xml {{[ed|edit]}} {{[-m|--move]}} "{{XPATH1}}" "{{XPATH2}}" {{path/to/input.xml|uri}}`

- Վերանվանել «id» անունով բոլոր ատրիբուտները «ID»՝:

`xml {{[ed|edit]}} {{[-r|--rename]}} "{{//*/@id}}" -v "{{ID}}" {{path/to/input.xml|uri}}`

- Վերանվանել «աղյուսակ» տարրի ենթատարրերը, որոնք ստացել են «rec» անվանումը «գրառման».:

`xml {{[ed|edit]}} {{[-r|--rename]}} "{{/xml/table/rec}}" -v "{{record}}" {{path/to/input.xml|uri}}`

- Թարմացրեք XML աղյուսակի գրառումը «id=3»-ով «id=5» արժեքով.:

`xml {{[ed|edit]}} {{[-u|--update]}} "{{xml/table/rec[@id=3]/@id}}" {{[-v|--value]}} {{5}} {{path/to/input.xml|uri}}`

- Ցուցադրել օգնությունը.:

`xml {{[ed|edit]}} {{[-h|--help]}}`

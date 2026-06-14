# xml ընտրեք

> Ընտրեք XML փաստաթղթերից՝ օգտագործելով XPATH:.
> Հուշում. օգտագործեք `xml elements` XML փաստաթղթի XPATH-ները ցուցադրելու համար:.
> Լրացուցիչ տեղեկություններ. <https://xmlstar.sourceforge.net/doc/UG/xmlstarlet-ug.html#idm47077139652416>:.

- Ընտրեք «XPATH1»-ին համապատասխանող բոլոր տարրերը և տպեք դրանց «XPATH2» ենթատարրի արժեքը.:

`xml {{[sel|select]}} {{[-t|--template]}} {{[-m|--match]}} "{{XPATH1}}" {{[-v|--value-of]}} "{{XPATH2}}" {{path/to/input.xml|uri}}`

- Համեմատեք «XPATH1» և տպեք «XPATH2» արժեքը որպես տեքստ նոր տողերով.:

`xml {{[sel|select]}} {{[-T|--text]}} {{[-t|--template]}} {{[-m|--match]}} "{{XPATH1}}" {{[-v|--value-of]}} "{{XPATH2}}" {{[-n|--nl]}} {{path/to/input.xml|uri}}`

- Հաշվեք «XPATH1»-ի տարրերը.:

`xml {{[sel|select]}} {{[-t|--template]}} {{[-v|--value-of]}} "count({{XPATH1}})" {{path/to/input.xml|uri}}`

- Հաշվեք բոլոր հանգույցները մեկ կամ մի քանի XML փաստաթղթերում.:

`xml {{[sel|select]}} {{[-T|--text]}} {{[-t|--template]}} {{[-f|--inp-name]}} {{[-o|--output]}} " " {{[-v|--value-of]}} "count(node())" {{[-n|--nl]}} {{path/to/input1.xml|uri}} {{path/to/input2.xml|uri}}`

- Ցուցադրել օգնությունը.:

`xml {{[sel|select]}} --help`

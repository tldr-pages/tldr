# xml տարրեր

> Արտահանել տարրեր և ցուցադրել XML փաստաթղթի կառուցվածքը:.
> Լրացուցիչ տեղեկություններ. <https://xmlstar.sourceforge.net/doc/UG/xmlstarlet-ug.html#idm47077139665568>:.

- Քաղեք տարրեր XML փաստաթղթից (արտադրելով XPATH արտահայտություններ).:

`xml {{[el|elements]}} {{path/to/input.xml|uri}} > {{path/to/elements.xpath}}`

- Քաղեք տարրերը և դրանց հատկանիշները XML փաստաթղթից.:

`xml {{[el|elements]}} -a {{path/to/input.xml|uri}} > {{path/to/elements.xpath}}`

- Քաղեք տարրերը և դրանց ատրիբուտներն ու արժեքները XML փաստաթղթից.:

`xml {{[el|elements]}} -v {{path/to/input.xml|uri}} > {{path/to/elements.xpath}}`

- Տպեք տեսակավորված եզակի տարրեր XML փաստաթղթից՝ դրա կառուցվածքը տեսնելու համար.:

`xml {{[el|elements]}} -u {{path/to/input.xml|uri}}`

- Տպեք տեսակավորված եզակի տարրեր XML փաստաթղթից մինչև 3 խորություն:

`xml {{[el|elements]}} -d{{3}} {{path/to/input.xml|uri}}`

- Ցուցադրել օգնությունը.:

`xml {{[el|elements]}} --help`

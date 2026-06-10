# xml վավերացնել

> Վավերացնել XML փաստաթղթերը:.
> Լրացուցիչ տեղեկություններ. <https://xmlstar.sourceforge.net/doc/UG/xmlstarlet-ug.html#idm47077139576400>:.

- Վավերացրեք մեկ կամ մի քանի XML փաստաթղթեր միայն լավ ձևավորված լինելու համար.:

`xml {{[val|validate]}} {{path/to/input1.xml|uri1 path/to/input2.xml|uri2 ...}}`

- Վավերացնել մեկ կամ մի քանի XML փաստաթղթեր՝ համաձայն փաստաթղթի տեսակի սահմանման (DTD).:

`xml {{[val|validate]}} {{[-d|--dtd]}} {{path/to/schema.dtd}} {{path/to/input1.xml|uri1 path/to/input2.xml|uri2 ...}}`

- Վավերացրեք մեկ կամ մի քանի XML փաստաթղթեր՝ ընդդեմ XML սխեմայի սահմանման (XSD).:

`xml {{[val|validate]}} {{[-s|--xsd]}} {{path/to/schema.xsd}} {{path/to/input1.xml|uri1 path/to/input2.xml|uri2 ...}}`

- Վավերացրեք մեկ կամ մի քանի XML փաստաթղթեր Relax NG սխեմայի (RNG) դեմ.:

`xml {{[val|validate]}} {{[-r|--relaxng]}} {{path/to/schema.rng}} {{path/to/input1.xml|uri1 path/to/input2.xml|uri2 ...}}`

- Ցուցադրել օգնությունը.:

`xml {{[val|validate]}} --help`

# zapier փայտամած

> Ավելացրեք մեկնարկային գործարկիչ, ստեղծեք, որոնեք կամ ռեսուրս ինտեգրմանը:.
> Լրացուցիչ տեղեկություններ. <https://platform.zapier.com/reference/cli#scaffold>:.

- Ստեղծեք նոր ձգան, ստեղծեք, որոնեք կամ ռեսուրս.:

`zapier scaffold {{trigger|search|create|resource}} {{noun}}`

- Նշեք մաքսային նպատակակետ գրացուցակ փայտամած ֆայլերի համար.:

`zapier scaffold {{trigger|search|create|resource}} {{noun}} {{[-d|--dest]}}={{path/to/directory}}`

- Վերագրեք գոյություն ունեցող ֆայլերը փայտամածների ժամանակ.:

`zapier scaffold {{trigger|search|create|resource}} {{noun}} {{[-f|--force]}}`

- Բացառել մեկնաբանությունները փայտամած ֆայլերից.:

`zapier scaffold {{trigger|search|create|resource}} {{noun}} --no-help`

- Ցույց տալ վրիպազերծման լրացուցիչ արդյունքը.:

`zapier scaffold {{[-d|--debug]}}`

# Բերքահավաք

> Գործիք, որը նախատեսված է ներթափանցման փորձարկման վաղ փուլերում օգտագործելու համար:.
> Լրացուցիչ տեղեկություններ. <https://github.com/laramies/theHarvester>:.

- Google-ի միջոցով տեղեկություններ հավաքեք տիրույթի վերաբերյալ.:

`theHarvester --domain {{domain_name}} --source google`

- Հավաքեք տեղեկատվություն տիրույթի վերաբերյալ՝ օգտագործելով բազմաթիվ աղբյուրներ.:

`theHarvester --domain {{domain_name}} --source {{duckduckgo,bing,crtsh}}`

- Փոխել արդյունքների սահմանաչափը աշխատելու համար.:

`theHarvester --domain {{domain_name}} --source {{google}} --limit {{200}}`

- Պահպանեք արդյունքը XML և HTML ձևաչափով երկու ֆայլերի մեջ.:

`theHarvester --domain {{domain_name}} --source {{google}} --file {{output_file_name}}`

- Ցուցադրել օգնությունը.:

`theHarvester --help`

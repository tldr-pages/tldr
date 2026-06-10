# qgis_process

> Գործարկեք QGIS մշակման ալգորիթմները հրամանի տողից՝ առանց GUI բացելու:.
> Տես նաև՝ `qgis`:.
> Լրացուցիչ տեղեկություններ. <https://docs.qgis.org/latest/en/docs/user_manual/processing/standalone.html>:.

- Թվարկեք բոլոր առկա մշակման ալգորիթմները.:

`qgis_process list`

- Ցուցադրել օգնություն հատուկ ալգորիթմի համար.:

`qgis_process help {{algorithm_id}}`

- Գործարկեք մշակման ալգորիթմ պարամետրերով.:

`qgis_process run {{algorithm_id}} {{--PARAMETER1=value1 --PARAMETER2=value2 ...}}`

- Գործարկեք ալգորիթմ և թողարկեք արդյունքներ որպես JSON:

`qgis_process --json run {{algorithm_id}} {{--PARAMETER1=value1 --PARAMETER2=value2 ...}}`

- Գործարկել առանց պլագինների բեռնման ավելի արագ գործարկման համար.:

`qgis_process --skip-loading-plugins run {{algorithm_id}} {{--PARAMETER1=value1 --PARAMETER2=value2 ...}}`

- Գործարկեք առանց գլխի սերվերի վրա առանց ցուցադրման.:

`QT_QPA_PLATFORM=offscreen qgis_process run {{algorithm_id}} {{--PARAMETER1=value1 --PARAMETER2=value2 ...}}`

- Ցուցակեք մատչելի և ակտիվ հավելումները.:

`qgis_process plugins`

- Միացնել կամ անջատել տեղադրված փլագինը.:

`qgis_process plugins {{enable|disable}} {{plugin_name}}`

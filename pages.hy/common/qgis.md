# qgis

> Դիտեք, ստեղծեք և վերլուծեք աշխարհագրական տվյալները Աշխարհագրական տեղեկատվական համակարգում:.
> Աջակցում է ռաստերներին, վեկտորներին և նախագծի ֆայլերին (`.qgs`, `.qgz`, `.qlr`):.
> Լրացուցիչ տեղեկություններ. <https://docs.qgis.org/latest/en/docs/user_manual/introduction/qgis_configuration.html#running-qgis-with-advanced-settings>:.

- Գործարկել QGIS:

`qgis`

- Բացեք կոնկրետ նախագծի ֆայլ.:

`qgis {{[-p|--project]}} {{path/to/project.qgz}}`

- Անմիջապես բացեք մեկ կամ մի քանի ռաստեր կամ վեկտորային ֆայլեր.:

`qgis {{path/to/file1.tif path/to/file2.shp ...}}`

- Թաքցնել էկրանը գործարկման ժամանակ.:

`qgis {{[-n|--nologo]}}`

- Սահմանեք նախնական քարտեզի չափը.:

`qgis {{[-e|--extent]}} {{xmin,ymin,xmax,ymax}}`

- Գործարկել Python սկրիպտը բեռնվածության վրա.:

`qgis {{[-f|--code]}} {{path/to/script.py}}`

- Գործարկել QGIS-ը առանց պլագինների վերականգնման.:

`qgis {{[-P|--noplugins]}}`

- Նախագիծ բացելիս բաց թողեք բացակայող շերտերի հուշումները.:

`qgis {{[-B|--skipbadlayers]}} {{[-p|--project]}} {{path/to/project.qgz}}`

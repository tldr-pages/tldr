# in2csv

> Փոխարկեք տարբեր աղյուսակային տվյալների ձևաչափեր CSV-ի:.
> Ներառված է csvkit-ում:.
> Լրացուցիչ տեղեկություններ. <https://csvkit.readthedocs.io/en/latest/scripts/in2csv.html>:.

- Փոխարկեք XLS ֆայլը CSV-ի.:

`in2csv {{data.xls}}`

- Փոխակերպեք DBF ֆայլը CSV ֆայլի.:

`in2csv {{data.dbf}} > {{data.csv}}`

- Փոխակերպեք որոշակի թերթիկ XLSX ֆայլից CSV:

`in2csv --sheet={{sheet_name}} {{data.xlsx}}`

- Խողովակավորեք JSON ֆայլը in2csv:

`cat {{data.json}} | in2csv {{[-f|--format]}} json > {{data.csv}}`

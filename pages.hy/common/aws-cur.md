# aws cur

> Ստեղծեք, հարցրեք և ջնջեք AWS-ի օգտագործման հաշվետվության սահմանումները:.
> Լրացուցիչ տեղեկություններ. <https://docs.aws.amazon.com/cli/latest/reference/cur/>:.

- Ստեղծեք AWS ծախսերի և օգտագործման հաշվետվության սահմանում JSON ֆայլից.:

`aws cur put-report-definition --report-definition file://{{path/to/report_definition.json}}`

- Թվարկեք օգտագործման հաշվետվության սահմանումները, որոնք սահմանված են մուտք գործած հաշվի համար.:

`aws cur describe-report-definitions`

- Ջնջել օգտագործման հաշվետվության սահմանումը.:

`aws cur --region {{aws_region}} delete-report-definition --report-name {{report}}`

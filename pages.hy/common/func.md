#ֆունկ

> Azure Functions Հիմնական գործիքներ. մշակեք և փորձարկեք Azure գործառույթները տեղական մակարդակում:.
> Տեղական գործառույթները կարող են միանալ կենդանի Azure ծառայություններին և կարող են գործառական հավելված տեղադրել Azure-ի բաժանորդագրության մեջ:.
> Լրացուցիչ տեղեկություններ. <https://learn.microsoft.com/azure/azure-functions/functions-run-local>:.

- Ստեղծեք նոր գործառույթների նախագիծ.:

`func init {{project}}`

- Ստեղծեք նոր գործառույթ.:

`func new`

- Գործարկեք գործառույթները տեղում.:

`func start`

- Հրապարակեք ձեր կոդը Azure-ի գործառույթային հավելվածում.:

`func azure functionapp publish {{function}}`

- Ներբեռնեք բոլոր կարգավորումները գոյություն ունեցող գործառույթի հավելվածից.:

`func azure functionapp fetch-app-settings {{function}}`

- Ստացեք կապի տողը հատուկ պահպանման հաշվի համար.:

`func azure storage fetch-connection-string {{storage_account}}`

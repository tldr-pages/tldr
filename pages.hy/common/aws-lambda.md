# aws lambda

> Օգտագործեք AWS Lambda-ն՝ հաշվողական ծառայություն՝ կոդ գործարկելու համար՝ առանց սերվերների տրամադրման կամ կառավարման:.
> Լրացուցիչ տեղեկություններ. <https://docs.aws.amazon.com/cli/latest/reference/lambda/>:.

- Գործարկել գործառույթը.:

`aws lambda invoke --function-name {{name}} {{path/to/response.json}}`

- Գործարկեք JSON ձևաչափով մուտքային բեռնվածությամբ ֆունկցիա.:

`aws lambda invoke --function-name {{name}} --payload {{json}} {{path/to/response.json}}`

- Ցանկի գործառույթները.:

`aws lambda list-functions`

- Ցուցադրել ֆունկցիայի կոնֆիգուրացիան.:

`aws lambda get-function-configuration --function-name {{name}}`

- Ցուցակեք ֆունկցիայի կեղծանունները.:

`aws lambda list-aliases --function-name {{name}}`

- Ցուցադրել վերապահված համաժամանակյա կոնֆիգուրացիան ֆունկցիայի համար.:

`aws lambda get-function-concurrency --function-name {{name}}`

- Նշեք, թե որ AWS ծառայությունները կարող են գործարկել գործառույթը.:

`aws lambda get-policy --function-name {{name}}`

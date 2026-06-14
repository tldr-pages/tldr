# pulumi սխեմա

> Ստուգեք Pulumi փաթեթի սխեման սխալների համար:.
> Սխեմայի հղում՝ <https://www.pulumi.com/docs/iac/extending-pulumi/schema/>:.
> Լրացուցիչ տեղեկություններ. <https://www.pulumi.com/docs/iac/cli/commands/pulumi_schema/>:.

- Ստուգեք փաթեթի սխեման.:

`pulumi schema check {{path/to/file}}`

- Ստուգեք փաթեթի սխեման առանց ձախողման, եթե որևէ տեսակի հղումը բացակայում է.:

`pulumi schema check --allow-dangling-references {{path/to/file}}`

- Ցուցադրել օգնությունը.:

`pulumi schema check {{[-h|--help]}}`

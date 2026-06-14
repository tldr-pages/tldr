# pulumi վիճակ

> Խմբագրել ընթացիկ փաթեթի վիճակը:.
> Լրացուցիչ տեղեկություններ. <https://www.pulumi.com/docs/iac/cli/commands/pulumi_state/>:.

- Ջնջել ռեսուրսը ընթացիկ փաթեթի վիճակից.:

`pulumi state delete`

- Տեղափոխեք ռեսուրսը ընթացիկ կույտից մյուսը.:

`pulumi state move {{resource_urn}} --dest {{stack_name}}`

- Վերանվանել ռեսուրսը ընթացիկ փաթեթի վիճակում.:

`pulumi state rename`

- Վերականգնել անվավեր վիճակը.:

`pulumi state repair`

- Խմբագրել փաթեթի վիճակը խմբագրիչում, որը նշված է `$EDITOR` միջավայրի փոփոխականով.:

`pulumi state edit --stack {{stack_name}}`

- Ցուցադրել օգնությունը.:

`pulumi state {{[-h|--help]}}`

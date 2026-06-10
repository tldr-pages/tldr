# pulumi env

> Կառավարեք Pulumi միջավայրերը:.
> Լրացուցիչ տեղեկություններ. <https://www.pulumi.com/docs/iac/cli/commands/pulumi_env/>:.

- Թվարկեք բոլոր միջավայրերը.:

`pulumi env ls`

- Ստեղծել միջավայր.:

`pulumi env init {{environment_name}}`

- Սահմանեք արժեք միջավայրում.:

`pulumi env set {{environment_name}} {{key}} {{value}}`

- Խմբագրել շրջակա միջավայրի սահմանումը.:

`pulumi env edit {{environment_name}}`

- Ջնջել արժեքը միջավայրից.:

`pulumi env rm {{environment_name}} {{key}}`

- Ամբողջովին ջնջել միջավայրը.:

`pulumi env rm {{environment_name}}`

- Ցուցադրել օգնությունը.:

`pulumi env {{[-h|--help]}}`

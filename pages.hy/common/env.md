#նախանձ

> Ցույց տալ միջավայրը կամ գործարկել ծրագիր փոփոխված միջավայրում:.
> Լրացուցիչ տեղեկություններ. <https://www.gnu.org/software/coreutils/manual/html_node/env-invocation.html>:.

- Ցույց տալ շրջակա միջավայրը.:

`env`

- Գործարկել ծրագիր: Հաճախ օգտագործվում է shebang-ից հետո (#!) սկրիպտներում՝ ծրագրի ուղին փնտրելու համար.:

`env {{program}}`

- Մաքրել շրջակա միջավայրը և գործարկել ծրագիր.:

`env {{[-i|--ignore-environment]}} {{program}}`

- Հեռացրեք փոփոխականը միջավայրից և գործարկեք ծրագիր.:

`env {{[-u|--unset]}} {{variable}} {{program}}`

- Սահմանեք փոփոխական և գործարկեք ծրագիր.:

`env {{variable}}={{value}} {{program}}`

- Սահմանեք մեկ կամ մի քանի փոփոխական և գործարկեք ծրագիր.:

`env {{variable1=value variable2=value variable3=value ...}} {{program}}`

- Գործարկել ծրագիր այլ անունով.:

`env {{[-a|--argv0]}} {{custom_name}} {{program}}`

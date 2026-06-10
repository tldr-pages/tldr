# arthas-հետք

> Հետագծել մեթոդի կանչի շղթան և թողարկել ժամանակի արժեքը ճանապարհի յուրաքանչյուր հանգույցի համար:.
> Տես նաև՝ `arthas`, `arthas-watch`:.
> Լրացուցիչ տեղեկություններ. <https://arthas.aliyun.com/en/doc/trace.html>:.

- Հետագծման մեթոդի կանչի շղթա.:

`trace {{class-pattern}} {{method-pattern}}`

- Հետագծել մեթոդի կանչի շղթաները և ցուցադրել միայն 10 ms-ից երկար կանչի մասին տեղեկատվությունը.:

`trace {{class-pattern}} {{method-pattern}} '#cost > {{10}}'`

- Հետևեք բազմաթիվ դասերի կամ բազմաթիվ մեթոդների կանչերի շղթային.:

`trace -E {{class-pattern1}}|{{class-patter2}} {{method-pattern1}}|{{method-pattern2}}|{{method-pattern3}}`

- Հետևեք կանչի շղթաներին, ցուցադրեք միայն 10 ms-ը գերազանցող տեղեկությունները և դուրս եկեք 5 անգամից հետո.:

`trace {{class-pattern}} {{method-pattern}} '#cost > {{10}}' -n 5`

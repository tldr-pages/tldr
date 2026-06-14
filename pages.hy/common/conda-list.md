# կոնդաների ցուցակ

> Ցուցակեք տեղադրված փաթեթները conda միջավայրում:.
> Լրացուցիչ տեղեկություններ. <https://docs.conda.io/projects/conda/en/stable/commands/list.html>:.

- Թվարկեք բոլոր փաթեթները ընթացիկ միջավայրում.:

`conda list`

- Նշեք փաթեթները նշված միջավայրում.:

`conda list {{[-n|--name]}} {{environment}}`

- Ցուցակեք տվյալ ուղու վրա տեղադրված փաթեթները.:

`conda list {{[-p|--prefix]}} {{path/to/environment}}`

- Զտել տեղադրված փաթեթները՝ օգտագործելով `regex`:

`conda list {{regex}}`

- Պահպանեք փաթեթները հետագա օգտագործման համար.:

`conda list {{[-e|--export]}} > {{path/to/package-list.txt}}`

# spf

> The superfile - Ժամանակակից տերմինալային ֆայլերի կառավարիչ:.
> Լրացուցիչ տեղեկություններ. <https://github.com/yorukot/superfile>:.

- Գործարկեք `spf`-ը կոնկրետ ճանապարհով.:

`spf {{path/to/directory}}`

- Գործարկեք `spf`-ը մի քանի ուղիներով.:

`spf {{path/to/directory1 path/to/directory2 ...}}`

- Ուղղեք թեժ ստեղների կարգավորումները՝ ավելացնելով բացակայող ստեղները.:

`spf {{[--fh|--fix-hotkeys]}}`

- Ուղղեք կազմաձևման ֆայլը՝ ավելացնելով բացակայող գրառումները.:

`spf {{[--fch|--fix-config-file]}}`

- Օգտագործեք հատուկ կազմաձևման և թեժ ստեղնաշարի ֆայլեր.:

`spf {{[-c|--config-file]}} {{path/to/config.toml}} {{[--hf|--hotkey-file]}} {{path/to/hotkey.toml}}`

- Գրեք առաջին ընտրված ֆայլի ուղին դեպի այս ֆայլ և դուրս եկեք.:

`spf {{[--cf|--chooser-file]}} {{tmp/chooser-result}}`

- Ցուցադրել ներքին կոնֆիգուրացիայի և տվյալների գրացուցակի ուղիները.:

`spf {{[pl|path-list]}}`

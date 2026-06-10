#պատգամավոր

> PHP-ի վրա հիմնված առաջադրանքների կառավարիչ Laravel-ի հեռավոր սերվերների համար:.
> Լրացուցիչ տեղեկություններ. <https://laravel.com/docs/envoy>:.

- Նախաձեռնեք կազմաձևման ֆայլը.:

`envoy init {{host_name}}`

- Գործարկել առաջադրանքը.:

`envoy run {{task_name}}`

- Գործարկել առաջադրանք կոնկրետ նախագծից.:

`envoy run --path {{path/to/directory}} {{task_name}}`

- Գործարկել առաջադրանքը և շարունակել ձախողումը.:

`envoy run --continue {{task_name}}`

- Թափել առաջադրանքը որպես Bash սցենար՝ ստուգման համար.:

`envoy run --pretend {{task_name}}`

- Միացեք նշված սերվերին SSH-ի միջոցով.:

`envoy ssh {{server_name}}`

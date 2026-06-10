# zeroclaw cron

> Կառավարեք պլանավորված առաջադրանքները ZeroClaw-ի համար:.
> Լրացուցիչ տեղեկություններ. <https://github.com/zeroclaw-labs/zeroclaw#quick-start>:.

- Թվարկեք բոլոր պլանավորված առաջադրանքները.:

`zeroclaw cron list`

- Ավելացրեք նոր պլանավորված առաջադրանք cron արտահայտությամբ.:

`zeroclaw cron add "{{* * * * *}}" "{{command}}"`

- Ավելացնել մեկ կրակոցով հետաձգված առաջադրանք.:

`zeroclaw cron once {{30m|1h|1d|...}} "{{command}}"`

- Հեռացրեք պլանավորված առաջադրանքը.:

`zeroclaw cron remove {{task_id}}`

- Դադարեցնել պլանավորված առաջադրանքը.:

`zeroclaw cron pause {{task_id}}`

- Վերսկսեք դադարեցված առաջադրանքը.:

`zeroclaw cron resume {{task_id}}`

- Ցուցադրել օգնությունը.:

`zeroclaw cron {{[-h|--help]}}`

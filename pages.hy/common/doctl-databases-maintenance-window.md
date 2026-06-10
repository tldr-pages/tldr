# doctl տվյալների բազաների սպասարկում-պատուհան

> Պլանավորեք և ստուգեք ձեր տվյալների բազաների սպասարկման պատուհանների ժամանակացույցը:.
> Լրացուցիչ տեղեկություններ. <https://docs.digitalocean.com/reference/doctl/reference/databases/maintenance-window/>:.

- Գործարկեք `doctl databases maintenance-window` հրամանը մուտքի նշանով.:

`doctl {{[d|databases]}} {{[mw|maintenance-window]}} {{command}} {{[-t|--access-token]}} {{access_token}}`

- Ստացեք տվյալների բազայի կլաստերի սպասարկման պատուհանների վերաբերյալ մանրամասներ.:

`doctl {{[d|databases]}} {{[mw|maintenance-window]}} {{[g|get]}} {{database_id}}`

- Թարմացրեք պահպանման պատուհանը տվյալների բազայի կլաստերի համար.:

`doctl {{[d|databases]}} {{[mw|maintenance-window]}} {{[u|update]}} {{database_id}} --day {{day_of_the_week}} --hour {{hour_in_24_hours_format}}`

# polybar-msg

> Կառավարեք `polybar`-ը՝ օգտագործելով միջգործընթացային հաղորդագրությունների փոխանակում (IPC):.
> Նշում. IPC-ն լռելյայն անջատված է և կարող է միացվել՝ Polybar-ի կազմաձևում սահմանելով `enable-ipc = true`:.
> Լրացուցիչ տեղեկություններ. <https://polybar.readthedocs.io/en/stable/user/ipc.html>:.

- Դուրս գալ բարից.:

`polybar-msg cmd quit`

- Վերագործարկեք բարը տեղում.:

`polybar-msg cmd restart`

- Թաքցնել բարը (ոչինչ չի անում, եթե բարն արդեն թաքնված է).:

`polybar-msg cmd hide`

- Կրկին ցուցադրեք գիծը (ոչինչ չի անում, եթե բարը թաքնված չէ):

`polybar-msg cmd show`

- Փոխարկել թաքնված/տեսանելի միջև.:

`polybar-msg cmd toggle`

- Կատարեք մոդուլի գործողություն (տվյալների տողը կամընտիր է).:

`polybar-msg action "#{{module_name}}.{{action_name}}.{{data_string}}"`

- Ուղարկեք հաղորդագրություններ միայն Polybar-ի կոնկրետ օրինակին (բոլոր օրինակները լռելյայն).:

`polybar-msg -p {{pid}} {{cmd|action}} {{payload}}`

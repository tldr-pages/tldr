# pg_walsummary

> Տպել WAL ամփոփ ֆայլերի բովանդակությունը:.
> Լրացուցիչ տեղեկություններ. <https://www.postgresql.org/docs/current/app-pgwalsummary.html>:.

- Վերափոխեք WAL ամփոփ ֆայլը տեքստի.:

`pg_walsummary {{path/to/file}}`

- Տպեք մեկ տող յուրաքանչյուր փոփոխված առանձին բլոկի համար (այլ ոչ թե միջակայքերը).:

`pg_walsummary {{[-i|--individual]}} {{path/to/file}}`

- ճնշել նորմալ ելքը (միայն սխալներ).:

`pg_walsummary {{[-q|--quiet]}} {{path/to/file}}`

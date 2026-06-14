# sdcv

> StarDict, բառարանի հաճախորդ:.
> Բառարանները տրամադրվում են պատվիրատուից առանձին:.
> Լրացուցիչ տեղեկություններ. <https://manned.org/sdcv>:.

- Սկսեք `sdcv` ինտերակտիվ կերպով.:

`sdcv`

- Տեղադրված բառարանների ցանկ.:

`sdcv --list-dicts`

- Ցուցադրել սահմանումը կոնկրետ բառարանից.:

`sdcv --use-dict {{dictionary_name}} {{search_term}}`

- Փնտրեք սահմանում մշուշոտ որոնմամբ.:

`sdcv {{search_term}}`

- Փնտրեք սահմանում ճշգրիտ որոնմամբ.:

`sdcv --exact-search {{search_term}}`

- Փնտրեք սահմանում և ձևաչափեք ելքը որպես JSON:

`sdcv --json {{search_term}}`

- Որոնեք բառարաններ որոշակի գրացուցակում.:

`sdcv --data-dir {{path/to/directory}} {{search_term}}`

#ճապ

> Կրկնօրինակման համակարգ՝ հիմնված Git packfile ձևաչափի վրա, որն ապահովում է լրացուցիչ պահումներ և գլոբալ կրկնօրինակում:.
> Լրացուցիչ տեղեկություններ. <https://manned.org/bup>:.

- Նախաձեռնեք պահուստային պահոցը տվյալ տեղական գրացուցակում.:

`bup {{[-d|--bup-dir]}} {{path/to/repository}} init`

- Նախքան կրկնօրինակում վերցնելը, պատրաստեք տվյալ գրացուցակը.:

`bup {{[-d|--bup-dir]}} {{path/to/repository}} index {{path/to/directory}}`

- Կրկնօրինակեք գրացուցակը պահեստում՝ նշելով դրա անունը.:

`bup {{[-d|--bup-dir]}} {{path/to/repository}} save {{[-n|--name]}} {{backup_name}} {{path/to/directory}}`

- Ցուցադրել պահոցում ներկայումս պահվող պահուստային նկարները.:

`bup {{[-d|--bup-dir]}} {{path/to/repository}} ls`

- Վերականգնել հատուկ պահուստային նկարը թիրախային գրացուցակում.:

`bup {{[-d|--bup-dir]}} {{path/to/repository}} restore {{[-C|--outdir]}} {{path/to/target_directory}} {{backup_name}}`

#իմմիչ

> Կառավարեք Immich սերվերները:.
> Տես նաև՝ `immich-go`:.
> Լրացուցիչ տեղեկություններ. <https://docs.immich.app/features/command-line-interface/>:.

- Նույնականացում Immich սերվերին.:

`immich login {{server_url/api}} {{server_key}}`

- Վերբեռնեք որոշ պատկերային ֆայլեր.:

`immich upload {{file1.jpg file2.jpg ...}}`

- Վերբեռնեք գրացուցակ, ներառյալ ենթագրքեր.:

`immich upload {{[-r|--recursive]}} {{path/to/directory}}`

- Ստեղծեք ալբոմ գրացուցակի հիման վրա.:

`immich upload {{[-r|--recursive]}} {{path/to/directory}} {{[-A|--album-name]}} "{{My summer holiday}}"`

- Բաց թողնել գլոբալ օրինաչափությանը համապատասխանող ակտիվները.:

`immich upload {{[-r|--recursive]}} {{path/to/directory}} {{[-i|--ignore]}} {{**/Raw/** **/*.tif}}`

- Ներառեք թաքնված ֆայլերը.:

`immich upload {{[-r|--recursive]}} {{path/to/directory}} {{[-H|--include-hidden]}}`

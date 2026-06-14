# get_iplayer

> Ինդեքսավորման գործիք և անձնական տեսաձայնագրիչ BBC iPlayer-ի և BBC Sounds-ի համար:.
> Լրացուցիչ տեղեկություններ. <https://github.com/get-iplayer/get_iplayer/wiki/manpage>:.

- Որոնել ծրագրեր անունով:

`get_iplayer "{{program_name}}"`

- Գրանցեք ծրագիրը ըստ որոնման արդյունքների.:

`get_iplayer "{{program_name}}" {{[-g|--get]}}`

- Գրանցեք ծրագիրը URL-ով BBC iPlayer կայքից.:

`get_iplayer "https://www.bbc.co.uk/iplayer/episode/{{program_pid}}/{{name-of-show-episode-number-episode-title}}"`

- Ներբեռնեք ենթագրեր ծրագրի համար ըստ որոնման արդյունքների.:

`get_iplayer "{{program_name}}" --subtitles-only`

- Որոնեք ծրագիր, ձայնագրեք այն և ներբեռնեք ենթագրեր.:

`get_iplayer "{{program_name}}" {{[-g|--get]}} --subtitles`

- Ցուցադրել օգնությունը.:

`get_iplayer {{[-h|--help]}}`

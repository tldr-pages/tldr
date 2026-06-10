# animdl

> Որոնեք, հեռարձակեք և ներբեռնեք անիմե:.
> Տես նաև՝ `ani-cli`:.
> Լրացուցիչ տեղեկություններ. <https://github.com/justfoolingaround/animdl#usage>:.

- Ներբեռնեք կոնկրետ անիմե.:

`animdl download "{{anime_title}}"`

- Ներբեռնեք կոնկրետ անիմե՝ նշելով դրվագների տիրույթը.:

`animdl download "{{anime_title}}" {{[-r|--range]}} {{start_episode}}-{{end_episode}}`

- Ներբեռնեք կոնկրետ անիմե՝ նշելով ներբեռնման գրացուցակը.:

`animdl download "{{anime_title}}" {{[-d|--download-dir]}} {{path/to/directory}}`

- Ձեռք բերեք հոսքի URL-ը կոնկրետ անիմեի համար.:

`animdl grab "{{anime_title}}"`

- Ցուցադրել առաջիկա անիմե ժամանակացույցը հաջորդ շաբաթվա համար.:

`animdl schedule`

- Որոնեք կոնկրետ անիմե.:

`animdl search "{{anime_title}}"`

- Հեռարձակեք կոնկրետ անիմե.:

`animdl stream "{{anime_title}}"`

- Հեռարձակեք կոնկրետ անիմեի վերջին դրվագը.:

`animdl stream "{{anime_title}}" {{[-s|--special]}} latest`

# ani-cli

> Զննեք և դիտեք անիմե:.
> Տես նաև՝ `animdl`:.
> Լրացուցիչ տեղեկություններ. <https://manned.org/ani-cli>:.

- Որոնել անիմե անունով:

`ani-cli "{{anime_title}}"`

- Ներբեռնեք դրվագ.:

`ani-cli {{[-d|--download]}} "{{anime_title}}"`

- Ներբեռնեք մի շարք դրվագներ.:

`ani-cli {{[-d|--download]}} {{[-r|--range]}} "{{1 6}}" "{{anime_title}}"`

- Ներբեռնեք ամբողջ շարքը (բոլոր դրվագների մի շարք).:

`ani-cli {{[-d|--download]}} {{[-r|--range]}} "1 -1" "{{anime_title}}"`

- Օգտագործեք VLC որպես մեդիա նվագարկիչ.:

`ani-cli {{[-v|--vlc]}} "{{anime_title}}"`

- Դիտեք կոնկրետ դրվագ.:

`ani-cli {{[-e|--episode]}} {{episode_number}} "{{anime_title}}"`

- Շարունակեք դիտել անիմե պատմությունից.:

`ani-cli {{[-c|--continue]}}`

- Թարմացնել `ani-cli`:

`ani-cli {{[-U|--update]}}`

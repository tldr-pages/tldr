# pio նախագիծ

> Կառավարեք PlatformIO նախագծերը:.
> Լրացուցիչ տեղեկություններ. <https://docs.platformio.org/en/latest/core/userguide/project/>:.

- Նախաձեռնեք նոր PlatformIO նախագիծ.:

`pio project init`

- Նախաձեռնեք նոր PlatformIO նախագիծը հատուկ գրացուցակում.:

`pio project init {{[-d|--project-dir]}} {{path/to/project_directory}}`

- Նախաձեռնեք նոր PlatformIO նախագիծ՝ նշելով տախտակի ID.:

`pio project init {{[-b|--board]}} {{ATmega328P|uno|...}}`

- Նախաձեռնեք նոր PlatformIO-ի վրա հիմնված նախագիծ՝ նշելով մեկ կամ մի քանի նախագծի տարբերակներ.:

`pio project init {{[-O|--project-option]}} "{{option}}={{value}}" {{[-O|--project-option]}} "{{option}}={{value}}"`

- Տպել նախագծի կոնֆիգուրացիան.:

`pio project config`

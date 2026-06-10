# pio run

> Գործարկել PlatformIO ծրագրի թիրախները:.
> Լրացուցիչ տեղեկություններ. <https://docs.platformio.org/en/latest/core/userguide/cmd_run.html>:.

- Թվարկեք բոլոր առկա ծրագրի թիրախները.:

`pio run --list-targets`

- Թվարկեք կոնկրետ միջավայրի բոլոր հասանելի ծրագրի թիրախները.:

`pio run --list-targets {{[-e|--environment]}} {{environment}}`

- Գործարկել բոլոր թիրախները.:

`pio run`

- Գործարկել նշված միջավայրերի բոլոր թիրախները.:

`pio run {{[-e|--environment]}} {{environment1}} {{[-e|--environment]}} {{environment2}}`

- Գործարկել նշված թիրախները.:

`pio run {{[-t|--target]}} {{target1}} {{[-t|--target]}} {{target2}}`

- Գործարկեք նշված կազմաձևման ֆայլի թիրախները.:

`pio run {{[-c|--project-conf]}} {{path/to/platformio.ini}}`

# pio թիմ

> Կառավարեք PlatformIO թիմերը:.
> Լրացուցիչ տեղեկություններ. <https://docs.platformio.org/en/latest/core/userguide/team/>:.

- Ստեղծեք նոր թիմ նշված նկարագրությամբ.:

`pio team create --description {{description}} {{organization_name}}:{{team_name}}`

- Ջնջել թիմը.:

`pio team destroy {{organization_name}}:{{team_name}}`

- Ավելացնել նոր օգտվող թիմին.:

`pio team add {{organization_name}}:{{team_name}} {{username}}`

- Հեռացրեք օգտվողին թիմից.:

`pio team remove {{organization_name}}:{{team_name}} {{username}}`

- Թվարկեք բոլոր թիմերը, որոնց անդամ է օգտատերը և նրանց անդամները.:

`pio team list`

- Նշեք կազմակերպության բոլոր թիմերը.:

`pio team list {{organization_name}}`

- Վերանվանել թիմը.:

`pio team update --name {{new_team_name}} {{organization_name}}:{{team_name}}`

- Փոխել թիմի նկարագրությունը.:

`pio team update --description {{new_description}} {{organization_name}}:{{team_name}}`

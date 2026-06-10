# pio օրգ

> Կառավարեք PlatformIO կազմակերպությունները և դրանց սեփականատերերը:.
> Լրացուցիչ տեղեկություններ. <https://docs.platformio.org/en/latest/core/userguide/org/>:.

- Ստեղծել նոր կազմակերպություն.:

`pio org create {{organization_name}}`

- Ջնջել կազմակերպությունը.:

`pio org destroy {{organization_name}}`

- Ավելացրեք օգտվող կազմակերպությանը.:

`pio org add {{organization_name}} {{username}}`

- Հեռացնել օգտատիրոջը կազմակերպությունից.:

`pio org remove {{organization_name}} {{username}}`

- Թվարկեք բոլոր կազմակերպությունները, որոնց անդամ է ներկա օգտվողը և դրանց սեփականատերերը.:

`pio org list`

- Թարմացրեք կազմակերպության անունը, էլ. փոստը կամ ցուցադրվող անունը.:

`pio org update --orgname {{new_organization_name}} --email {{new_email}} --displayname {{new_display_name}} {{organization_name}}`

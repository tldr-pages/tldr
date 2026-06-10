# wezterm

> Wez's Terminal Emulator - հզոր միջպլատֆորմային տերմինալային էմուլյատոր և մուլտիպլեքսոր:.
> Որոշ ենթահրամաններ, ինչպիսիք են `cli`-ն, ունեն իրենց օգտագործման փաստաթղթերը:.
> Լրացուցիչ տեղեկություններ. <https://wezterm.org/cli/general>:.

- Սկսեք նոր Wezterm գործընթաց և ստեղծեք պատուհան.:

`wezterm`

- Ստեղծեք `ssh` նիստ նոր Wezterm պատուհանում.:

`wezterm ssh {{user}}@{{host}}:{{port}}`

- Միացեք մուլտիպլեքսորին (`wezterm-mux-server`):

`wezterm connect {{domain_name}}`

- Արտադրեք պատկեր տերմինալում.:

`wezterm imgcat {{path/to/image}}`

- Գրանցեք տերմինալի նստաշրջանը որպես asciicast (լռելյայն ձայնագրությունները պահվում են `/tmp`-ում):

`wezterm record`

- Կրկնել asciicast տերմինալի նիստը.:

`wezterm replay {{path/to/cast_file}}`

- Նշեք օգտագործվող կազմաձևման ֆայլը (գերակայում է կազմաձևման ֆայլի նորմալ լուծումը).:

`wezterm --config-file {{path/to/config_file}}`

- Ցուցադրել օգնությունը.:

`wezterm help`

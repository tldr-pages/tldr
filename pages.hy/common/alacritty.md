#ալակրիտություն

> Խաչաձև հարթակ, GPU-ով արագացված տերմինալային էմուլյատոր:.
> Լրացուցիչ տեղեկություններ. <https://manned.org/alacritty>:.

- Սկսեք նոր Alacritty գործընթաց և ստեղծեք պատուհան.:

`alacritty`

- Սկսեք Alacritty daemon-ը (առանց պատուհան ստեղծելու).:

`alacritty --daemon`

- Ստեղծեք նոր պատուհան՝ օգտագործելով արդեն գործող Alacritty գործընթացը.:

`alacritty msg create-window`

- Սկսեք կեղևը որոշակի գրացուցակում (աշխատում է նաև `alacritty msg create-window`-ով):

`alacritty --working-directory {{path/to/directory}}`

- Կատարեք հրաման նոր Alacritty պատուհանում (աշխատում է նաև `alacritty msg create-window`-ով).:

`alacritty {{[-e|--command]}} {{command}}`

- Օգտագործեք այլընտրանքային կազմաձևման ֆայլ (կանխադրված է `$XDG_CONFIG_HOME/alacritty/alacritty.toml`):

`alacritty --config-file {{path/to/config.toml}}`

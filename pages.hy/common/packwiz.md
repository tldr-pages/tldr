# packwiz

> Ստեղծեք, խմբագրեք և կառավարեք Minecraft modpacks:.
> Լրացուցիչ տեղեկություններ. <https://packwiz.infra.link/reference/commands/packwiz/>:.

- Ինտերակտիվ կերպով ստեղծեք նոր modpack ընթացիկ գրացուցակում.:

`packwiz init`

- Ավելացրեք ռեժիմ Modrinth-ից կամ Curseforge-ից.:

`packwiz {{modrinth|curseforge}} add {{url|slug|search_term}}`

- Թվարկեք բոլոր ռեժիմները modpack-ում.:

`packwiz list`

- Թարմացրեք `index.toml` ֆայլերը ձեռքով խմբագրելուց հետո.:

`packwiz refresh`

- Արտահանել որպես Modrinth (`.mrpack`) կամ Curseforge (Zip) ֆայլ՝:

`packwiz {{modrinth|curseforge}} export`

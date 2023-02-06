# protontricks

> Egy egyszerű wrapper, amely Winetricks parancsokat futtat a Proton-kompatibilis játékokhoz. További információ: <https://github.com/Matoking/protontricks>.

- A protontricks GUI futtatása:

`protontricks --gui`

- Winetricks futtatása egy adott játékhoz:

`protontricks {{appid}} {{winetricks_args}}`

- Futtasson egy parancsot egy játék telepítési könyvtárában:

`protontricks -c {{command}} {{appid}}`

- \[l\]ist az összes telepített játék:

`protontricks -l`

- \[s\]earch for a game's App ID by name:

`protontricks -s {{game_name}}`

- A protontricks súgóüzenet megjelenítése:

`protontricks --help`

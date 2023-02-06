# for

> Egy parancs többszöri feltételes végrehajtása. További információ: <https://learn.microsoft.com/windows-server/administration/windows-commands/for>.

- Adott parancsok végrehajtása a megadott készletre:

`for %{{variable}} in ({{item_a item_b item_c}}) do ({{echo Loop is executed}})`

- Iterálás egy adott számtartományon:

`for /l %{{variable}} in ({{from}}, {{step}}, {{to}}) do ({{echo Loop is executed}})`

- Iterálás egy adott fájllistán:

`for %{{variable}} in ({{file_a.ext file_b.ext file_c.ext}}) do ({{echo Loop is executed}})`

- Iterálás könyvtárak adott listáján:

`for /d %{{variable}} in ({{directory_a/ directory_b/ directory_c/}}) do ({{echo Loop is executed}})`

- Adott parancs végrehajtása minden könyvtárban:

`for /d %{{variable}} in (*) do (if exist %{{variable}} {{echo Loop is executed}})`

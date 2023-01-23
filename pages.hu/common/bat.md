# bat

> Fájlok nyomtatása és összekapcsolása. `cat` klón szintaxis kiemeléssel és Git integrációval. További információ: <https://github.com/sharkdp/bat>.

- Egy fájl tartalmának kinyomtatása a standard kimenetre:

`bat {{path/to/file}}`

- Több fájl összefűzése a célfájlba:

`bat {{file1}} {{file2}} > {{target_file}}`

- Több fájl csatolása a célfájlba:

`bat {{file1}} {{file2}} >> {{target_file}}`

- Minden kimeneti sor számozása:

`bat --number {{path/to/file}}`

- JSON fájl szintaxiskiemelése:

`bat --language json {{file.json}}`

- Az összes támogatott nyelv megjelenítése:

`bat --list-languages`

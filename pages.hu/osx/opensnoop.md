# opensnoop

> Eszköz, amely nyomon követi a fájlmegnyitásokat a rendszerben. További információ: <https://ss64.com/osx/opensnoop.html>.

- Minden fájlmegnyitás kinyomtatása, amint az megtörténik:

`sudo opensnoop`

- Nyomon követheti egy folyamat által végrehajtott összes fájlmegnyitást név szerint:

`sudo opensnoop -n "{{process_name}}"`

- Nyomon követheti az összes fájlmegnyitást egy folyamat által PID szerint:

`sudo opensnoop -p {{PID}}`

- Nyomon követheti, hogy mely folyamatok nyitnak meg egy adott fájlt:

`sudo opensnoop -f {{path/to/file}}`

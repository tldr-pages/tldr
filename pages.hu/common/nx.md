# nx

> CLI segédprogram a `nx` munkaterületek kezeléséhez. További információ: <https://nx.dev/l/r/getting-started/nx-cli>.

- Egy adott projekt létrehozása:

`nx build {{project}}`

- Egy adott projekt tesztelése:

`nx test {{project}}`

- Célpont végrehajtása egy adott projekten:

`nx run {{project}}:{{target}}`

- Célpont végrehajtása több projekten:

`nx run-many --target {{target}} --projects {{project1}},{{project2}}`

- Célpont végrehajtása a munkaterület összes projektjén:

`nx run-many --target {{target}} --all`

- Célpont végrehajtása csak a módosított projekteken:

`nx affected --target {{target}}`

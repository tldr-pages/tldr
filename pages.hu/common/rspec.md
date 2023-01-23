# rspec

> Ruby nyelven írt viselkedésvezérelt fejlesztési tesztelési keretrendszer Ruby kód tesztelésére. További információ: <https://rspec.info>.

- Egy .rspec config és egy spec segédfájl inicializálása:

`rspec --init`

- Az összes teszt futtatása:

`rspec`

- A tesztek egy adott könyvtárának futtatása:

`rspec {{path/to/directory}}`

- Egy adott tesztfájl futtatása:

`rspec {{path/to/file}}`

- Több tesztfájl futtatása:

`rspec {{path/to/file1}} {{path/to/file2}}`

- Egy adott teszt futtatása egy fájlban (pl. a teszt a 83. sorban kezdődik):

`rspec {{path/to/file}}:{{83}}`

- Specifikációk futtatása egy adott maggal:

`rspec --seed {{seed_number}}`

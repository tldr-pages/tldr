# stdbuf

> Futtasson egy parancsot a szabványos adatfolyamok módosított pufferelési műveleteivel. További információ: <https://www.gnu.org/software/coreutils/stdbuf>.

- Módosítsa a szabványos bemeneti puffer méretét 512 KiB-ra:

`stdbuf --input={{512K}} {{command}}`

- Módosítsa a szabványos kimeneti puffert sorpufferesre:

`stdbuf --output={{L}} {{command}}`

- A standard hibapuffert változtassa puffer nélkülire:

`stdbuf --error={{0}} {{command}}`

# shc

> Generic shell script compilator.

- Compilați un script shell:

`shc -f {{script}}`

- Compilați un script shell și specificați un fișier binar de ieșire:

`shc -f {{script}} -o {{binary}}`

- Compilați un script shell și setați o dată de expirare pentru executabil:

`shc -f {{script}} -e {{dd/mm/yyyy}}`

- Compilați un script shell și setați un mesaj pentru a afișa la expirare:

`shc -f {{script}} -e {{dd/mm/yyyy}} -m "{{Please contact your provider}}"`

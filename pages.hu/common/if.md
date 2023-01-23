# if

> Feltételes feldolgozást végez shell szkriptekben. Lásd még: `test` `[` További információ: <https://www.gnu.org/software/bash/manual/bash.html#Conditional-Constructs>.

- A megadott parancsok végrehajtása, ha a feltételes parancs kilépési állapota nulla:

`if {{condition_command}}; then {{echo "Condition is true"}}; fi`

- A megadott parancsok végrehajtása, ha a feltételes parancs kilépési állapota nem nulla:

`if ! {{condition_command}}; then {{echo "Condition is true"}}; fi`

- Az első megadott parancsok végrehajtása, ha a feltételparancs kilépési állapota nulla, különben a második megadott parancsok végrehajtása:

`if {{condition_command}}; then {{echo "Condition is true"}}; else {{echo "Condition is false"}}; fi`

- Ellenőrizze, hogy létezik-e \[f\]ile:

`if [[ -f {{path/to/file}} ]]; then {{echo "Condition is true"}}; fi`

- Ellenőrizze, hogy létezik-e \[d\]irectory:

`if [[ -d {{path/to/directory}} ]]; then {{echo "Condition is true"}}; fi`

- Ellenőrizze, hogy létezik-e \[e\]xisz fájl vagy könyvtár:

`if [[ -e {{path/to/file_or_directory}} ]]; then {{echo "Condition is true"}}; fi`

- Ellenőrizze, hogy egy változó definiálva van-e:

`if [[ -n "${{variable}}" ]]; then {{echo "Condition is true"}}; fi`

- Az összes lehetséges feltétel felsorolása (`test` a `[` alias neve ; mindkettőt általában a `if` címmel együtt használják):

`man [`

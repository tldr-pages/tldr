# mmv

> Fájlok tömeges áthelyezése és átnevezése. További információ: <https://manned.org/mmv.1>.

- Az összes, bizonyos kiterjesztésű fájl átnevezése más kiterjesztésre:

`mmv "*{{.old_extension}}" "#1{{.new_extension}}"`

- A `report6part4.txt` másolása a `./french/rapport6partie4.txt` címre az összes hasonló nevű fájlal együtt:

`mmv -c "{{report*part*.txt}}" "{{./french/rapport#1partie#2.txt}}"`

- A `.txt` összes fájljának egy fájlba való csatolása:

`mmv -a "{{*.txt}}" "{{all.txt}}"`

- A fájlnevekben szereplő dátumokat "M-D-Y" formátumról "D-M-Y" formátumra alakítja át:

`mmv "{{[0-1][0-9]-[0-3][0-9]-[0-9][0-9][0-9][0-9].txt}}" "{{#3#4-#1#2-#5#6#7#8.txt}}"`

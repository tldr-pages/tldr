# ufraw-batch

> A fényképezőgépek RAW-fájljainak szabványos képfájlokká történő átalakítása. További információ: <https://manned.org/ufraw-batch>.

- Egyszerűen konvertálja a RAW-fájlokat JPG-be:

`ufraw-batch --out-type=jpg {{input_file(s)}}`

- Egyszerűen konvertálja a RAW-fájlokat PNG-be:

`ufraw-batch --out-type=png {{input_file(s)}}`

- Az előnézeti kép kivonása a nyers fájlból:

`ufraw-batch --embedded-image {{input_file(s)}}`

- A fájl mentése a megadott maximális MAX1 és MAX2 méretig:

`ufraw-batch --size=MAX1,MAX2 {{input_file(s)}}`

# vgmstream_cli

> A videojátékokban használt hangformátumok széles skáláját játszhatja le és konvertálhatja őket a `wav`. További információ: <https://vgmstream.org/doc/USAGE>.

- Egy `adc` fájl dekódolása `wav`. (Az alapértelmezett kimeneti név: `input.wav`):

`vgmstream_cli {{path/to/input.adc}} -o {{path/to/output.wav}}`

- Metaadatok nyomtatása a hang dekódolása nélkül:

`vgmstream_cli {{path/to/input.adc}} -m`

- Hurok nélküli hangfájl dekódolása:

`vgmstream_cli {{path/to/input.adc}} -o {{path/to/output.wav}} -i`

- Dekódolás három hurokkal, majd hozzáad egy 3 másodperces késleltetést, amelyet egy 5 másodperces fadeout követ:

`vgmstream_cli {{path/to/input.adc}} -o {{path/to/output.wav}} -l {{3.0}} -f {{5.0}} -d {{3.0}}`

- Több fájl konvertálása `bgm_(original name).wav` (Az alapértelmezett `-o` minta a `?f.wav`):

`vgmstream_cli -o {{path/to/bgm_?f.wav}} {{path/to/file1.adc}} {{path/to/file2.adc}}`

- A fájl végtelenített hurokban történő lejátszása (`channels` és `rate` metaadatoknak meg kell egyezniük):

`vgmstream_cli {{path/to/input.adc}} -pec | aplay --format cd --channels {{1}} --rate {{44100}}`

# sox

> Sound eXchange: hangfájlok lejátszása, felvétele és konvertálása. A hangformátumokat a kiterjesztés azonosítja. További információ: <http://sox.sourceforge.net>.

- Két hangfájl egyesítése eggyé:

`sox -m {{input_audiofile1}} {{input_audiofile2}} {{output_audiofile}}`

- Egy hangfájl vágása a megadott időkre:

`sox {{input_audiofile}} {{output_audiofile}} trim {{start}} {{end}}`

- Egy hangfájl normalizálása (hangerő beállítása a maximális csúcsszintre, vágás nélkül):

`sox --norm {{input_audiofile}} {{output_audiofile}}`

- Egy hangfájl visszafordítása és mentése:

`sox {{input_audiofile}} {{output_audiofile}} reverse`

- Egy hangfájl statisztikai adatainak nyomtatása:

`sox {{input_audiofile}} -n stat`

- Egy hangfájl hangerejének kétszeresére növelése:

`sox -v 2.0 {{input_audiofile}} {{output_audiofile}}`

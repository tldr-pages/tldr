# ufraw-batch

> Conversia fișierelor RAW din camere în fișiere imagine standard.

- Pur și simplu convertiți fișierele RAW în jpg:

`ufraw-batch --out-type=jpg {{input_file(s)}}`

- Pur și simplu convertiți fișierele RAW la png:

`ufraw-batch --out-type=png {{input_file(s)}}`

- Extrageţi imaginea de previzualizare din fişierul brut:

`ufraw-batch --embedded-image {{input_file(s)}}`

- Salvați fișierul cu o dimensiune de până la maximele date MAX1 și MAX2:

`ufraw-batch --size=MAX1,MAX2 {{input_file(s)}}`

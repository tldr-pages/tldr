# pbmreduce

> Verklein een PBM afbeelding proportioneel.
> Zie ook: `pamenlarge`, `pamditherbw`.
> Meer informatie: <https://netpbm.sourceforge.net/doc/pbmreduce.html>.

- Verklein de gespecificeerde afbeelding met de gespecificeerde factor:

`pbmreduce {{n}} {{pad/naar/afbeelding.pbm}} > {{pad/naar/uitvoer.pbm}}`

- Gebruik eenvoudige thresholding bij het verkleinen:

`pbmreduce {{[-t|-threshold]}} {{n}} {{pad/naar/afbeelding.pbm}} > {{pad/naar/uitvoer.pbm}}`

- Gebruik de gespecificeerde drempelwaarde voor alle kwantisaties:

`pbmreduce {{[-va|-value]}} {{0.6}} {{n}} {{pad/naar/afbeelding.pbm}} > {{pad/naar/uitvoer.pbm}}`

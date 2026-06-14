# pnmindex

> Կառուցեք բազմաթիվ PNM պատկերների տեսողական ինդեքս:.
> Տես նաև՝ `pamundice`:.
> Լրացուցիչ տեղեկություններ. <https://netpbm.sourceforge.net/doc/pnmindex.html>:.

- Ցանցում արտադրեք նշված պատկերների մանրապատկերները պարունակող պատկեր.:

`pnmindex {{path/to/input1.pnm path/to/input2.pnm ...}} > {{path/to/output.pnm}}`

- Նշեք (քառակուսի) մանրապատկերների չափը.:

`pnmindex {{[-s|-size]}} {{50}} {{path/to/input1.pnm path/to/input2.pnm ...}} > {{path/to/output.pnm}}`

- Նշեք յուրաքանչյուր տողի մանրապատկերների քանակը.:

`pnmindex {{[-a|-across]}} {{10}} {{path/to/input1.pnm path/to/input2.pnm ...}} > {{path/to/output.pnm}}`

- Նշեք ելքի մեջ գույների առավելագույն քանակը.:

`pnmindex {{[-c|-colors]}} {{512}} {{path/to/input1.pnm path/to/input2.pnm ...}} > {{path/to/output.pnm}}`

# xml validate

> XML dokumentumok validálása. További információ: <http://xmlstar.sourceforge.net/docs.php>.

- Egy vagy több XML-dokumentum validálása csak a jólformáltság szempontjából:

`xml validate {{path/to/input1.xml|URI}} {{input2.xml ...}}`

- Egy vagy több XML-dokumentum hitelesítése egy dokumentumtípus-definíció (DTD) alapján:

`xml validate --dtd {{path/to/schema.dtd}} {{path/to/input1.xml|URI}} {{input2.xml ...}}`

- Egy vagy több XML-dokumentum hitelesítése XML-sémadefiníció (XSD) alapján:

`xml validate --xsd {{path/to/schema.xsd}} {{path/to/input1.xml|URI}} {{input2.xml ...}}`

- Egy vagy több XML-dokumentum hitelesítése egy Relax NG séma (RNG) alapján:

`xml validate --relaxng {{path/to/schema.rng}} {{path/to/input1.xml|URI}} {{input2.xml ...}}`

- A `validate` alparancs súgójának megjelenítése:

`xml validate --help`

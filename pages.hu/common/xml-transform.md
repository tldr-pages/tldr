# xml transform

> XML dokumentumok átalakítása XSLT segítségével. További információ: <http://xmlstar.sourceforge.net/docs.php>.

- Egy XML-dokumentum átalakítása XSL-stíluslap segítségével, egy XPATH paraméter és egy szó szerinti karakterlánc paraméter átadásával:

`xml transform {{path/to/stylesheet.xsl}} -p "{{Count='count(/xml/table/rec)'}}" -s {{Text="Count="}} {{path/to/input.xml|URI}}`

- A `transform` alparancs súgójának megjelenítése:

`xml transform --help`

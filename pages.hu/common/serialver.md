# serialver

> Visszaadja az osztályok serialVersionUID-jét. Alapértelmezés szerint nem állít be biztonsági kezelőt. További információ: <https://docs.oracle.com/en/java/javase/19/docs/specs/man/serialver.html>.

- Egy osztály serialVersionUID-jének megjelenítése:

`serialver {{classnames}}`

- Osztályok és erőforrások kettősponttal elválasztott listájának serialVersionUID-jének megjelenítése:

`serialver -classpath {{path/to/directory}} {{classname1:classname2:...}}`

- A Java-alkalmazás indítójának referenciaoldaláról a Java Virtual Machine-re vonatkozó speciális opció használata:

`serialver -Joption {{classnames}}`

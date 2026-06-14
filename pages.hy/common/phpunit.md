# phpunit

> PHPUnit թեստային վազորդ:.
> Լրացուցիչ տեղեկություններ. <https://docs.phpunit.de/en/12.4/textui.html#command-line-options>:.

- Գործարկել թեստերը ընթացիկ գրացուցակում: Նշում. ակնկալում է, որ դուք կունենաք `phpunit.xml'`:

`phpunit`

- Գործարկել թեստերը հատուկ ֆայլում.:

`phpunit {{path/to/TestFile.php}}`

- Գործարկել տվյալ խմբի հետ ծանոթագրված թեստերը.:

`phpunit --group {{name}}`

- Գործարկեք թեստեր և ստեղծեք ծածկույթի հաշվետվություն HTML-ում.:

`phpunit --coverage-html {{path/to/directory}}`

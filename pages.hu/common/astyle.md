# astyle

> Forráskód indentáló, formázó és szépítő program a C, C++, C# és Java programozási nyelvekhez. Futtatásakor az eredeti fájl másolata jön létre, az eredeti fájl nevéhez egy ".orig"-ot csatolva. További információ: <http://astyle.sourceforge.net/>.

- Alkalmazza az alapértelmezett stílust: 4 szóköz behúzásonként, és nem változtat a formázáson:

`astyle {{source_file}}`

- Alkalmazza a Java-stílust csatolt zárójelekkel:

`astyle --style=java {{path/to/file}}`

- Alkalmazza az allman stílust szaggatott zárójelekkel:

`astyle --style=allman {{path/to/file}}`

- Egyéni behúzás alkalmazása szóközökkel. Válasszon 2 és 20 szóköz között:

`astyle --indent=spaces={{number_of_spaces}} {{path/to/file}}`

- Egyéni behúzás alkalmazása tabulátorok használatával. Válasszon 2 és 20 tabulátor között:

`astyle --indent=tab={{number_of_tabs}} {{path/to/file}}`

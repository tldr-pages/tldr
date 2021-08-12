# xmllint

> Parser XML și linter care acceptă XPath, o sintaxă pentru navigarea copacilor XML.

- Returnează toate nodurile (etichete) numite „foo”:

`xmllint --xpath "//{{foo}}" {{source_file.xml}}`

- Returnați conținutul primului nod numit „foo” ca șir:

`xmllint --xpath "string(//{{foo}})" {{source_file.xml}}`

- Returnați atributul href al celui de-al doilea element de ancorare într-un fișier html:

`xmllint --html --xpath "string(//a[2]/@href)" webpage.xhtml`

- Întoarce XML lizibil de om (indentat) din fișier:

`xmllint --format {{source_file.xml}}`

- Verificați dacă un fișier XML îndeplinește cerințele declarației sale DOCTYPE:

`xmllint --valid {{source_file.xml}}`

- Validează XML împotriva schema DTD găzduit online:

`xmllint --dtdvalid {{URL}} {{source_file.xml}}`

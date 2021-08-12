# zip

> Ambalați și comprimați (arhivați) fișierele în fișier zip.

- Ambalarea și comprimarea fișierelor și directoarelor [r] ecursiv:

`zip -r {{compressed.zip}} {{path/to/file}} {{path/to/directory1}} {{path/to/directory2}}`

- E [x] clude fișierele nedorite de la a fi adăugate la arhiva comprimată:

`zip -r {{compressed.zip}} {{path/to/directory}} -x {{path/to/exclude}}`

- Arhivați un director și conținutul său cu cel mai înalt nivel [9] de compresie:

`zip -r -{{9}} {{compressed.zip}} {{path/to/directory}}`

- Creați o arhivă criptată (utilizatorul va fi solicitat o parolă):

`zip -e -r {{compressed.zip}} {{path/to/directory}}`

- Adăugați fișiere la un fișier zip existent:

`zip {{compressed.zip}} {{path/to/file}}`

- Ștergeți fișierele dintr-un fișier zip existent:

`zip -d {{compressed.zip}} "{{foo/*.tmp}}"`

- Arhivați un director și conținutul său într-un fișier zip (de exemplu, piese de 3 GB) multi-part:

`zip -r -s {{3g}} {{compressed.zip}} {{path/to/directory}}`

- Lista fișierelor dintr-o arhivă specificată (fără a le extrage):

`zip -sf {{compressed.zip}}`

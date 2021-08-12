# unrar

> Extrageți arhivele RAR.

- Extragerea fișierelor cu structura directorului original:

`unrar x {{compressed.rar}}`

- Extragerea fișierelor pe o cale specificată cu structura directorului original:

`unrar x {{compressed.rar}} {{path/to/extract}}`

- Extrageți fișiere în directorul curent, pierzând structura directorului în arhivă:

`unrar e {{compressed.rar}}`

- Testarea integrității fiecărui fișier în interiorul fișierului de arhivă:

`unrar t {{compressed.rar}}`

- Lista fișierelor din interiorul fișierului de arhivă fără a le decomprima:

`unrar l {{compressed.rar}}`

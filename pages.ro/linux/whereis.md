# whereis

> Găsiți fișierele de pagină binare, sursă și manual pentru o comandă.

- Localizați paginile binare, sursă și om pentru ssh:

`whereis {{ssh}}`

- Localizați paginile binare și om pentru ls:

`whereis -bm {{ls}}`

- Găsiți sursa de gcc și pagini de om pentru Git:

`whereis -s {{gcc}} -m {{git}}`

- Localizați binare pentru gcc numai în `/usr/bin/`:

`whereis -b -B {{/usr/bin/}} -f {{gcc}}`

- Localizați binare neobișnuite (cele care au mai mult sau mai puțin de un binar pe sistem):

`whereis -u *`

- Localizați binare care au intrări manuale neobișnuite (binare care au mai mult sau mai puțin de un manual instalat):

`whereis -u -m *`

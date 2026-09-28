# whereis

> Zoek de binary-, bron- en manualbestanden voor een commando.
> Zie ook: `which`, `whatis`, `type`.
> Meer informatie: <https://manned.org/whereis>.

- Zoek binary, bron en man-pagina's voor SSH:

`whereis {{ssh}}`

- Zoek [b]inary en [m]an-pagina's voor ls:

`whereis -bm {{ls}}`

- Zoek [s]ource van gcc en [m]an-pagina's voor Git:

`whereis -s {{gcc}} -m {{git}}`

- Zoek [b]inaries voor gcc alleen in `/usr/bin/`:

`whereis -b -B {{/usr/bin/}} -f {{gcc}}`

- Zoek [u]ngewone binaries (die meer of minder dan één binary op het systeem hebben):

`whereis -u *`

- Zoek binaries met [u]ngewone [m]anual-vermeldingen (binaries die meer of minder dan één manual geïnstalleerd hebben):

`whereis -u -m *`

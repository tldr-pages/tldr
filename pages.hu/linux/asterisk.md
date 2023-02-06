# asterisk

> Telefon és telefonközpont (telefon) szerver. Magának a szervernek a futtatására és egy már futó példány kezelésére szolgál. További információ: <https://wiki.asterisk.org/wiki/display/AST/Home>.

- \[R\]econnect to a running server, and turn on logging 3 levels of \[v\]erbosity:

`asterisk -r -vvv`

- \[R\]econnect to a running server, run a single command, and return:

`asterisk -r -x "{{command}}"`

- A chan_SIP-ügyfelek (telefonok) megjelenítése:

`asterisk -r -x "sip show peers"`

- Aktív hívások és csatornák megjelenítése:

`asterisk -r -x "core show channels"`

- Hangposta postafiókok megjelenítése:

`asterisk -r -x "voicemail show users"`

- Csatorna megszüntetése:

`asterisk -r -x "hangup request {{channel_ID}}"`

- A chan_SIP konfiguráció újratöltése:

`asterisk -r -x "sip reload"`

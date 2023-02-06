# newsboat

> RSS/Atom feed olvasó szöveges terminálokhoz. További információ: <https://newsboat.org/>.

- Először importálja a feed URL-címeket egy OPML-fájlból:

`newsboat -i {{my-feeds.xml}}`

- Alternatívaként adjon hozzá feedeket manuálisan:

`echo {{http://example.com/path/to/feed}} >> "${HOME}/.newsboat/urls"`

- Indítsa el a newsboat-ot, és indításkor frissítse az összes feedet:

`newsboat -r`

- Parancsok szóközzel elválasztott listájának végrehajtása nem interaktív módban:

`newsboat -x {{reload print-unread ...}}`

- Lásd a billentyűparancsok (a legfontosabbak az állapotsorban láthatók):

`?`

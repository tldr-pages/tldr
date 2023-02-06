# xsltproc

> XML átalakítása XSLT-vel, hogy kimenetet (általában HTML vagy XML) állítson elő. További információ: <http://www.xmlsoft.org/xslt/xsltproc.html>.

- XML-fájl átalakítása egy adott XSLT-stíluslap segítségével:

`xsltproc --output {{output.html}} {{stylesheet.xslt}} {{xmlfile.xml}}`

- Adjon át egy értéket a stíluslap egyik paraméterének:

`xsltproc --output {{output.html}} --stringparam "{{name}}" "{{value}}" {{stylesheet.xslt}} {{xmlfile.xml}}`

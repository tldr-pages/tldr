# xsltproc

> Przekształcanie XML z XSLT w celu uzyskania wyjścia (zwykle HTML lub XML).
> Więcej informacji: <http://www.xmlsoft.org/xslt/xsltproc.html>.

- Przekształcenie pliku XML za pomocą określonego arkusza stylów XSLT:

`xsltproc --output {{sciezka/do/pliku_wyjscia.html}} {{sciezka/do/arkusza_stylow.xslt}} {{sciezka/do/pliku.xml}}`

- Przekaż wartość do parametru w arkuszu stylów:

`xsltproc --output {{sciezka/do/pliku_wyjscia.html}} --stringparam "{{nazwa}}" "{{wartosc}}" {{sciezka/do/arkusza_stylow.xslt}} {{sciezka/do/pliku.xml}}`

# xsltproc

> Przekształć XML z XSLT w celu uzyskania wyjścia (zwykle HTML lub XML).
> Więcej informacji: <https://manned.org/xsltproc>.

- Przekształć plik XML za pomocą określonego arkusza stylów XSLT:

`xsltproc --output {{ścieżka/do/pliku_wyjścia.html}} {{ścieżka/do/arkusza_stylów.xslt}} {{ścieżka/do/pliku.xml}}`

- Przekaż wartość do parametru w arkuszu stylów:

`xsltproc --output {{ścieżka/do/pliku_wyjścia.html}} --stringparam "{{nazwa}}" "{{wartość}}" {{ścieżka/do/arkusza_stylów.xslt}} {{ścieżka/do/pliku.xml}}`

# chroma

> A Chroma egy általános célú szintaxiskiemelő könyvtár és a hozzá tartozó parancs, Go számára. További információ: <https://github.com/alecthomas/chroma>.

- Forrásfájl kiemelése python lexerrel és kimenet a terminálba:

`chroma --lexer="{{python}}" {{source_file}}`

- Forrásfájl kiemelése a Go lexerrel és kimenet egy HTML fájlba:

`chroma --lexer="{{go}}" --formatter="{{html}}" {{source_file}} > {{html_file}}`

- Forrásfájl kiemelése a C++ lexerrel és kimenet egy SVG-be, a Monokai stílus használatával:

`chroma --lexer="{{c++}}" --formatter="{{svg}}" --syle="{{monokai}}" {{source_file}} > {{svg_file}}`

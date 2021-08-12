# chroma

> Chroma este o bibliotecă de evidențiere a sintaxei de uz general și o comandă corespunzătoare, pentru Go.
> Mai multe informaţii: <https://github.com/alecthomas/chroma>

- Evidenţiaţi un fişier sursă cu Python Lexer şi ieşire la terminal:

`chroma --lexer="{{python}}" {{source_file}}`

- Evidențiați un fișier sursă cu Go lexer și ieșiți într-un fișier HTML:

`chroma --lexer="{{go}}" --formatter="{{html}}" {{source_file}} > {{html_file}}`

- Evidențiați un fișier sursă cu C++ lexer și ieșiți într-o imagine SVG, folosind stilul Monokai:

`chroma --lexer="{{c++}}" --formatter="{{svg}}" --syle="{{monokai}}" {{source_file}} > {{svg_file}}`

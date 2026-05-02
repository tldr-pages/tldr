# grep

> Caută tipare în fișiere folosind expresii regulate (`regex`).
> Vezi și: `regex`.
> Mai multe informații: <https://www.gnu.org/software/grep/manual/grep.html>.

- Caută un tipar într-un set de fișiere:

`grep "{{tipar_de_căutare}}" {{cale/către/fișier1 cale/către/fișier2 ...}}`

- Caută un șir de caractere exact (dezactivează `regex`-ul):

`grep {{[-F|--fixed-strings]}} "{{șir_exact}}" {{cale/către/fișier}}`

- Caută un tipar recursiv în toate fișierele dintr-un folder, ignorând fișierele binare:

`grep {{[-rI|--recursive --binary-files=without-match]}} "{{tipar_de_căutare}}" {{cale/către/folder}}`

- Afișează 3 linii de [C]ontext (în jur, î[B]ainte sau [A]fter de fiecare potrivire):

`grep {{--context|--before-context|--after-context}} 3 "{{tipar_de_căutare}}" {{cale/către/fișier}}`

- Afișează numele fișierului și numărul liniei pentru fiecare potrivire, cu ieșire colorată:

`grep {{[-Hn|--with-filename --line-number]}} --color=always "{{tipar_de_căutare}}" {{cale/către/fișier}}`

- Afișează doar textul potrivit:

`grep {{[-o|--only-matching]}} "{{tipar_de_căutare}}" {{cale/către/fișier}}`

- Citește datele din `stdin` și nu afișează liniile care se potrivesc cu tiparul:

`cat {{cale/către/fișier}} | grep {{[-v|--invert-match]}} "{{tipar_de_căutare}}"`

- Folosește `regex` extins (suportă `?`, `+`, `{}`, `()` și `|`), în mod insensibil la majuscule:

`grep {{[-Ei|--extended-regexp --ignore-case]}} "{{tipar_de_căutare}}" {{cale/către/fișier}}`

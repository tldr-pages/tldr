# pygmentize

> Evidențiator de sintaxă bazat pe Pyton.

- Evidențiați sintaxa fișierului și imprimați la ieșirea standard (limba este dedusă din extensia fișierului):

`pygmentize {{file.py}}`

- Setați în mod explicit limba pentru evidențierea sintaxei:

`pygmentize -l {{javascript}} {{input_file}}`

- Lexere disponibile (procesoare pentru limbi de intrare):

`pygmentize -L lexers`

- Salvați ieșirea într-un fișier în format HTML:

`pygmentize -f html -o {{output_file.html}} {{input_file.py}}`

- Lista formatelor de ieșire disponibile:

`pygmentize -L formatters`

- Ieșiți un fișier HTML, cu opțiuni suplimentare de formatare (pagină completă, cu numere de linie):

`pygmentize -f html -O "full,linenos=True" -o {{output_file.html}} {{input_file}}`

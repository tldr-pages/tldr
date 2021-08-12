# mmdc

> CLI pentru sirenă, un instrument de generare de diagrame cu un limbaj specific domeniului.
> Un fișier de definiție sirenă este luat ca intrare și un fișier SVG, PNG sau PDF este generat ca ieșire.
> Mai multe informaţii: <https://mermaid-js.github.io/mermaid/>

- Conversia unui fișier în formatul specificat (determinat automat din extensia fișierului):

`mmdc --input {{input.mmd}} --output {{output.svg}}`

- Specificați tema graficului:

`mmdc --input {{input.mmd}} --output {{output.svg}} --theme {{forest|dark|neutral|default}}`

- Specificați culoarea de fundal a graficului (de exemplu, `lime`, `” #D8064F „` sau `transparent`):

`mmdc --input {{input.mmd}} --output {{output.svg}} --backgroundColor {{color}}`
